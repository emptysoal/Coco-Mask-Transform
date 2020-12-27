# -*- coding:utf-8 -*-

"""
    从类似 Superpixel 的标注结果中分离出各个类别
"""

import os
import glob
import cv2 as cv
import numpy as np

from config import Config


def gray2masks(label_name):
    lbl_id = os.path.split(label_name)[-1].split('.')[0]
    idx = 0
    lbl = np.load(label_name)

    for label in Config.GRAY_DICT:
        mask = lbl == label
        if mask.sum() > 0:  # 图像中含有该类别
            binary = np.zeros(lbl.shape[:2], dtype=np.uint8)
            binary[mask] = 255
            mask_name = "%s%s_%s_0.png" % (Config.MASK_DIR, lbl_id, Config.GRAY_DICT[label])
            assert os.path.exists(os.path.dirname(mask_name)), "单通道 mask 存储路径不存在，请修改配置文件。"
            cv.imwrite(mask_name, binary)


label_dir = Config.LABEL_DIR
label_list = glob.glob(os.path.join(label_dir, '*.npy'))
for label_name in label_list:
    gray2masks(label_name)
