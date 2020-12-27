"""
    3通道的彩色标注结果（如labelme结果），变为单通道的标注结果（类似于superpixel结果）
"""

import cv2 as cv
import numpy as np

# 红色：键盘，标记为1，绿色：鼠标，标记为2
label_dict = {(0, 0, 128): 1, (0, 128, 0): 2}

img_path = "../mask2coco/labels/1.png"

img = cv.imread(img_path)
img_r = img[:, :, 2]
img_g = img[:, :, 1]
img_b = img[:, :, 0]

binary = np.zeros(img.shape[:2], dtype=np.uint8)

for color in label_dict:
    mask_r = img_r == color[2]
    mask_g = img_g == color[1]
    mask_b = img_b == color[0]

    mask = np.bitwise_and(np.bitwise_and(mask_r, mask_g), mask_b)
    if mask.sum() > 0:  # # 图像中含有该类别
        binary[mask] = label_dict[color]

np.save("label", binary)

cv.imshow("binary", binary)
# cv.imwrite("test.png", binary)

cv.waitKey()
