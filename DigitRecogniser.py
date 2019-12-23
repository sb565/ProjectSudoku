import cv2
import numpy as np
import pytesseract


def Digit_Detector():

	output = []

	for i in range(81):
		namei = "numbers/" + str(i) + ".png"
		im = cv2.imread(namei)	
		im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
		im = cv2.bitwise_not(im,im)
		e_chk = im.copy()
		e_chk = cv2.bitwise_not(e_chk,e_chk)
		ret, e_chk = cv2.threshold(e_chk, 127, 255, 0)
		contours, hierarchy = cv2.findContours(e_chk, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		if len(contours) == 0:
			output.append(0)
		else:
			digit = pytesseract.image_to_string(im, lang='eng', config='--oem 3 --psm 10 outputbase digits')
			if digit not in ['1','2','3','4','5','6','7','8','9']:
				digit = '0'
			output.append(int(digit))

	output = np.array(output)
	output.shape = (9,9)
	output = output.T
	result = output.copy()
	output = np.reshape(output,(81))
	f = open("input.txt","w+")
	f.write("\n".join(str(item) for item in output))
	f.close()
	return result