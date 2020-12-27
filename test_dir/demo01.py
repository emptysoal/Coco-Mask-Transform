import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_path = "../mask2coco/labels/1.png"

img = cv.imread(img_path)
print(img.shape)

binary = np.zeros(img.shape[:2], dtype=np.uint8)

img_r = img[:, :, 2]
img_g = img[:, :, 1]
img_b = img[:, :, 0]

mask_r = img_r == 128
mask_g = img_g == 0
mask_b = img_b == 0

mask = np.bitwise_and(np.bitwise_and(mask_r, mask_g), mask_b)
print(mask.sum())

binary[mask] = 255

cv.imshow("binary", binary)
cv.imwrite("test.png", binary)
plt.imsave("test2.png", img)

cv.waitKey()
