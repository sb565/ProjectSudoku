import cv2
from keras.models import load_model
import numpy as np

output = []

model = load_model('cnn.h5')

for i in range(81):
    namei = "numbers/" + str(i) + ".png"
    im = cv2.imread(namei)
    
    im = imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    e_chk = im.copy()
    ret, e_chk = cv2.threshold(e_chk, 127, 255, 0)
    contours, hierarchy = cv2.findContours(e_chk, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        output.append(0)
    else:
        image = np.array(im ,'float64')
        image.shape = (1,28,28,1)
        result = model.predict(image, batch_size=1)
        
        output.append(np.argmax(result))
output = np.array(output)
output.shape = (9,9)
output = output.T
print(output)
output = np.reshape(output,(81))
f = open("input.txt","w+")
f.write("\n".join(str(item) for item in output))
f.close()