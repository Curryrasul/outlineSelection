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

g1 = [
    [1, 0],
    [0, -1]
]

g2 = [
    [0, 1],
    [-1, 0]
]

for i in range(1, width):
    for j in range(1, height):
        gradient1 = (
            g1[0][0] * img[j - 1][i - 1] + 
            g1[1][1] * img[j][i]
        )
        
        gradient2 = ( 
            g2[0][1] * img[j - 1][i] + 
            g2[1][0] * img[j][i - 1]
        )

        gradientMagn = math.sqrt(gradient1 * gradient1 + gradient2 * gradient2)
        img2[j][i] = gradientMagn

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('Original image')

plt.subplot(122)
plt.imshow(img2, cmap = 'gray')
plt.title('Roberts operator')

plt.show()