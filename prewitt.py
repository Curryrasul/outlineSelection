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

gx = [
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
]

gy = [
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]
]

for i in range(1, width - 1):
    for j in range(1, height - 1):
        gradientX = (
            gx[0][0] * img[j - 1][i - 1] + 
            gx[0][2] * img[j - 1][i + 1] + 
            gx[1][0] * img[j][i - 1] + 
            gx[1][2] * img[j][i + 1] + 
            gx[2][0] * img[j + 1][i - 1] + 
            gx[2][2] * img[j + 1][i + 1]
        )
        
        gradientY = ( 
            gy[0][0] * img[j - 1][i - 1] + 
            gy[0][1] * img[j - 1][i] + 
            gy[0][2] * img[j - 1][i + 1] + 
            gy[2][0] * img[j + 1][i - 1] + 
            gy[2][1] * img[j + 1][i] + 
            gy[2][2] * img[j + 1][i + 1]
        )

        gradientMagn = math.sqrt(gradientX * gradientX + gradientY * gradientY)
        img2[j][i] = gradientMagn

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Original image')

plt.subplot(122)
plt.imshow(img2, cmap = 'gray')
plt.title('Prewitt operator')

plt.show()