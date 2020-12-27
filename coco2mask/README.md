# Coco 标注格式转化为 Mask 格式

## 参考

`https://blog.csdn.net/qq_44943603/article/details/107699207`

## 文件说明

- data：
  - coco：
    - annotations：coco 标注格式的 json 文件 ；
    - images：原始图像
  - coco_mask:
    - mask_images：存放二值化 mask 图像；
    - mask_images_RGBA：四通道图像
- coco2mask.py：把 coco格式转为 mask 图，不区分类别；
- coco2mask_1channel.py：把 coco格式转为单通道 mask 图，类似SuperPixel输出格式；
- coco2mask_1channel.py：把 coco格式转为三通道 mask 图，类似Labelme输出格式；
- draw_mask.py：把 mask 图显示到原图上；
- config.py：配置文件。

## 使用

1. 把coco格式的json文件放入annotations目录下；

2. 修改配置文件

   根据自己需求修改

3. 启动运行环境：

```bash
$ cd ~/coco_mask_transform/
$ docker run -it -v $PWD:/workspace pycocotools:v1
# cd /workspace/coco2mask
```

3. 运行程序

```bash
# python coco2mask.py
```

