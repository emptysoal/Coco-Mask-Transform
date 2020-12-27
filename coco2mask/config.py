# -*- coding:utf-8 -*-


class Config:
    CLASS_NAMES = ['keyboard', 'mouse']
    SAVE_DIR = "data/coco_mask/"
    ANN_FILE = "data/coco/annotations/coco_res.json"

    # 颜色和类别的对应关系
    COLOR_DICT = {
        (128, 0, 0): "keyboard",
        (0, 128, 0): "mouse"
    }
    COLOR_DICT_INV = {
        1: [128, 0, 0],
        2: [0, 128, 0]
    }
    GRAY_DICT = {
        1: "keyboard",
        2: "mouse"
    }
