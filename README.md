# HBB Remote Sensing Object Detection

Horizontal object detection on remote sensing data sets with the new mmdetection.

Explore benchmark for comparison.

Personal maintenance and use.

### Support Dataset
- DIOR

### Support Model
- YOLOv3 (darknet53)
- Faster RCNN (resnet50+fpn)



## Prepare Env

```shell
conda create -n mmdet_dior python=3.8
conda activate mmdet_dior

conda install -c pytorch pytorch torchvision
# or
pip3 install torch torchvision

pip install openmim
mim install mmengine 'mmcv>=2.0.0rc0' 'mmdet>=3.0.0rc0'
```



## Results

| Detector                                                     | AP50 | APs  | APm  | APl  |
| ------------------------------------------------------------ | ---- | ---- | ---- | ---- |
| [YOLO v3 (darknet53, 320)](configs/yolov3/yolov3_d53_2xb32-320-273e_dior.py) | 55.8 | 9.2  | 42.7 | 81.1 |
| [YOLO v3 (darknet53, ms-608)](configs/yolov3/yolov3_d53_2xb4-ms-608-273e_dior.py) | 57.4 | 21.6 | 49.5 | 74.5 |
| [Faster RCNN (resnet50+fpn)](configs/faster_rcnn/faster-rcnn_r50_fpn_2xb2-50e_dior.py) |      |      |      |      |

