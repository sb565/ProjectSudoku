import preprocess
from mnist_predictor import Prediction_Nummbers
import cv2
import numpy as np
import keras


input_file = "Images/input1.jpeg"
model_name = "cnn.h5"

#using tricode
original = cv2.imread(input_file, cv2.IMREAD_GRAYSCALE)
processed = preprocess.pre_process_image(original)
corners = preprocess.find_corners_of_largest_polygon(processed)
cropped = preprocess.crop_and_warp(original, corners)
squares = preprocess.infer_grid(cropped)
digits = preprocess.get_digits(cropped, squares, 28)
#digits has the shape (81,28,28) where 81 different digits are of size 28X28
for i in range(81):
	namei = "numbers/" + str(i) + ".png"
	cv2.imwrite(namei,digits[i])
preprocess.show_digits(digits)

Prediction_Nummbers(model_name)