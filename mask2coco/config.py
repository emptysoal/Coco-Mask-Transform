# -*- coding:utf-8 -*-

"""
    mask 转 coco 的配置文件
        根据自己需求修改
"""


class Config:
    """生成的二值化 mask 相关"""
    LABEL_DIR = "./labels"  # 存放 ground truth，即图像标注结果
    MASK_DIR = "./annotations/"  # 最后一定加 "/"，存放由 labels 生成的二值化 mask 图

    # 颜色和类别的对应关系
    COLOR_DICT = {
        (0, 0, 128): "keyboard",
        (0, 128, 0): "mouse"
    }
    GRAY_DICT = {
        1: "keyboard",
        2: "mouse"
    }

    """生成 coco 格式的 json 相关"""
    IMAGE_DIR = "./images"  # 存放原始图像
    COCO_JSON = "./coco_json_result/result.json"  # coco 标注格式的结果
    # 类别和类别号对应
    CATEGORIES = [
        {
            'id': 1,
            'name': 'keyboard',
            'supercategory': 'hardware',
        },
        {
            'id': 2,
            'name': 'mouse',
            'supercategory': 'hardware',
        }
    ]
