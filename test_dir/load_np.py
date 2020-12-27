import numpy as np
import cv2 as cv

# np_data = np.load("label.npy")
np_data = np.load(
    "/Users/donghongda/Python/projects/to_coco/coco_mask_transform/coco2mask/data/coco_mask/mask_images/1.npy")
# print(list(np_data))

np_data[np_data == 1] = 8
np_data[np_data == 2] = 15

cv.imshow("qqq", np_data)
cv.waitKey()
