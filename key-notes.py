import cv2
import numpy

# in the terminal, enter "py -3.11 -m pip install opencv-python" (without the quotes) to install cv2
# Images are represented by numbers in matrix form. Each row of numbers represents the pixel of the image.
array = cv2.imread("image.png")
# print(array)  # this displays/ reads the matrix representation of the image

# creating an image when just given the matrix representation of it.
a = numpy.array([[[255, 0, 0],
                  [255, 255, 255],
                  [255, 255, 255],
                  [187, 41, 160]],

                 [[255, 255, 255],
                  [255, 255, 255],
                  [255, 255, 255],
                  [255, 255, 255]],

                 [[255, 255, 255],
                  [0, 0, 0],
                  [47, 255, 173],
                  [255, 255, 255]]])
cv2.imwrite("image.png", a)
