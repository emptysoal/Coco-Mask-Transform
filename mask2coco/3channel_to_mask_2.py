# -*- coding:utf-8 -*-

"""
    通过掩码方式从3通道标注结果中分离出各种颜色，
    每种颜色为一种类别
"""

import os
import glob
import cv2 as cv
import numpy as np

from config import Config


def rgb2masks(label_name):
    lbl_id = os.path.split(label_name)[-1].split('.')[0]
    idx = 0
    lbl = cv.imread(label_name, 1)
    lbl_r = lbl[:, :, 2]
    lbl_g = lbl[:, :, 1]
    lbl_b = lbl[:, :, 0]

    for color in Config.COLOR_DICT:
        mask_r = lbl_r == color[2]
        mask_g = lbl_g == color[1]
        mask_b = lbl_b == color[0]

        mask = np.bitwise_and(np.bitwise_and(mask_r, mask_g), mask_b)
        if mask.sum() > 0:  # 图像中含有该类别
            binary = np.zeros(lbl.shape[:2], dtype=np.uint8)
            binary[mask] = 255
            mask_name = "%s%s_%s_0.png" % (Config.MASK_DIR, lbl_id, Config.COLOR_DICT[color])
            assert os.path.exists(os.path.dirname(mask_name)), "单通道 mask 存储路径不存在，请修改配置文件。"
            cv.imwrite(mask_name, binary)


label_dir = Config.LABEL_DIR
label_list = glob.glob(os.path.join(label_dir, '*.png'))
for label_name in label_list:
    rgb2masks(label_name)
