import cv2 
import numpy as np
import math
from matplotlib import pyplot as plt
from PIL import Image
from PIL import ImageDraw
from PIL import ImageColor

img = cv2.imread('./images/brush.png', 0)

width = len(img[0])
height = len(img)

img2 = img.copy()

matrices = [
    [
        [5, 5, 5],
        [-3, 0, -3],
        [-3, -3, -3]
    ],

    [
        [5, 5, -3],
        [5, 0, -3],
        [-3, -3, -3]
    ],

    [
        [5, -3, -3],
        [5, 0, -3],
        [5, -3, -3]
    ],

    [
        [-3, -3, -3],
        [5, 0, -3],
        [5, 5, -3]
    ],

    [
        [-3, -3, -3],
        [-3, 0, -3],
        [5, 5, 5]
    ],

    [
        [-3, -3, -3],
        [-3, 0, 5],
        [-3, 5, 5]
    ],

    [
        [-3, -3, 5],
        [-3, 0, 5],
        [-3, -3, 5]
    ],

    [
        [-3, 5, 5],
        [-3, 0, 5],
        [-3, -3, -3]
    ],
]

for i in range(1, width - 1):
    for j in range(1, height - 1):
        img2[j][i] = -1000
        for matrix in matrices:
            temp = (
                matrix[0][0] * img[j - 1][i - 1] + 
                matrix[0][1] * img[j - 1][i] + 
                matrix[0][2] * img[j - 1][i + 1] + 
                matrix[1][0] * img[j][i - 1] + 
                matrix[1][2] * img[j][i + 1] + 
                matrix[2][0] * img[j + 1][i - 1] +
                matrix[2][1] * img[j + 1][i] + 
                matrix[2][2] * img[j + 1][i + 1]
            )

            if temp > img2[j][i]:
                img2[j][i] = temp

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Original image')

plt.subplot(122)
plt.imshow(img2, cmap = 'gray')
plt.title('Kirsch operator')

plt.show()