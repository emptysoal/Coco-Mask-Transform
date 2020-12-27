"""
    修改的地方:
        将image_path, mask_path改为自己的路径
"""
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import numpy as np
import torch
from torch.autograd import Variable
from torchvision.transforms import ToPILImage

# 输入tensor变量
# 输出PIL格式图片
# def tensor_to_PIL(tensor):
#     image = tensor.cpu().clone()
#     image = image.squeeze(0)
#     image = unloader(image)
#     return image


if __name__ == '__main__':
    image_path = 'data/coco/images/1.png'
    mask_path = 'data/coco_mask/mask_images/1.png'
    # image 原图
    # seg_image 分割图
    image = Image.open(image_path)
    seg_image = Image.open(mask_path)

    '''这段是我用于目标检测是用的数据类型转换,可以删除'''
    # iw, ih = image.size
    # h, w = 416, 416
    # seg_image = seg_image.resize((h,w),Image.BICUBIC)
    # seg = np.array(seg_image, dtype=np.float32)
    # tmp_seg_targets = np.transpose(seg / 255.0, (2, 0, 1))
    #
    # seg_output = Variable(torch.from_numpy(tmp_seg_targets).type(torch.FloatTensor))
    #
    #
    # print(seg_output)
    # unloader = ToPILImage()
    # img = tensor_to_PIL(seg_output)  # tensor转为PIL Image
    # img = img.resize((iw, ih), Image.BICUBIC)
    # img.show()  # 显示图片
    # union_image_mask(img,image)

    plt.imshow(image)
    plt.imshow(seg_image, alpha=0.4)  # alpha - 用于控制透明的程度
    plt.show()
