import cv2
import numpy as np
import os
import glob
from config import Config


def rgb2masks(label_name):
    lbl_id = os.path.split(label_name)[-1].split('.')[0]
    lbl = cv2.imread(label_name, 1)
    h, w = lbl.shape[:2]
    instance_dict = {}
    idx = 0
    white_mask = np.ones((h, w, 3), dtype=np.uint8) * 255
    for i in range(h):
        for j in range(w):
            if tuple(lbl[i][j]) in instance_dict or tuple(lbl[i][j]) == (0, 0, 0):
                continue
            instance_dict[tuple(lbl[i][j])] = idx
            mask = (lbl == lbl[i][j]).all(-1)
            # instance = lbl * mask[..., None]      # colorful leaf with black background
            # np.repeat(mask[...,None],3,axis=2)    # 3D mask
            instance = np.where(mask[..., None], white_mask, 0)
            mask_name = Config.MASK_DIR + lbl_id + Config.COLOR_DICT[tuple(lbl[i][j])] + str(idx) + '.png'
            assert os.path.exists(os.path.dirname(mask_name)), "单通道 mask 存储路径不存在，请修改配置文件。"
            cv2.imwrite(mask_name, instance)


label_dir = Config.LABEL_DIR
label_list = glob.glob(os.path.join(label_dir, '*.png'))
for label_name in label_list:
    rgb2masks(label_name)
