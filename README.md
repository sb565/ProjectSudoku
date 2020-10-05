# ProjectSudoku
Program to read the sudoku from image and then prepare the solved puzzle. 
This sudoku solver is unique in its own ways. It takes images of the unsolved sudoku grid on which we apply image processing to detect the grid and get each digit grid separately. Then these segmented digit images are resized to 28x28 and are recognised using the OCR. These recognised digits are used to solve the puzzle using backtracking, then the solution is presented.

## Requirements
### Python3 Libraries 
opencv

operator

numpy

pytesseract

### Other Dependencies
tesseract-ocr engine

## Screenshots

![HomeScreen Screenshot](/Screenshots/HomeScreen.png?raw=true "Home Screen")

![OCR Screenshot](/Screenshots/OCR.png?raw=true "Recognised Digits")

![Results Screenshot](/Screenshots/Results.png?raw=true "Solved Puzzle")