# Mask 格式的分割结果转化为 Coco 标注格式

## 参考

`https://blog.csdn.net/francislucien2017/article/details/90407093`

## 文件说明

- images：存放原始图像，手动放入；

- labels：存放 ground truth，即图像标注结果，手动放入；
- annotations：存放由 labels 生成的二值化 mask 图，代码生成；
- coco_json_result：存放 coco 标注格式的结果；
- pycococreatortools：封装 pycocotools 的代码；
- 1channel_to_mask.py：把单通道 labels 生成二值化 mask 图；
- 3channel_to_mask.py：把三通道 labels 生成二值化 mask 图；
- 3channel_to_mask_2.py：把三通道 labels 生成二值化 mask 图，推荐使用，速度更快；
- shapes_to_coco.py：把二值化 mask 图生成为 coco 格式的结果；
- config.py：配置文件。

## 使用

1. 把原始图像和mask标注结果分别放入images和labels目录下；

   备注：**文件名必须是数字**

2. 修改配置文件

   根据自己需求修改

3. 启动运行环境：

```bash
$ cd ~/coco_mask_transform/
$ docker run -it -v $PWD:/workspace pycocotools:v1
# cd /workspace/mask2coco
```

3. 运行程序

```bash
# python to_mask.py
# python shapes_to_coco.py
```

