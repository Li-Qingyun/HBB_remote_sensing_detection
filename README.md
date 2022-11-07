# HBB Remote Sensing Object Detection

Horizontal object detection on remote sensing data sets with the mmdetection of OpenMMLab 2.0.

Explore benchmark for comparison.

Personal maintenance and use.

### Support Dataset
- DIOR

### Support Model
- YOLOv3 (darknet53)
- Faster RCNN (resnet50+fpn)



## Prepare Env

```shell
# create env
conda create -n mmdet_dior python=3.8
conda activate mmdet_dior

# install pytorch
conda install -c pytorch pytorch torchvision
# or
pip3 install torch torchvision

# install mmdet of OpenMMLab 2.0
pip install openmim
mim install mmengine 'mmcv>=2.0.0rc0' 'mmdet>=3.0.0rc0'
```



## Launch Experiments

Using [mim](https://github.com/open-mmlab/mim) to deal with experiments.

```shell
# training
mim train mmdet {config}  # train on single gpu
mim train mmdet {config} --cfg-options train_dataloader.batch_size=1  # modify cfg options
mim train mmdet {config} --gpus {num_gpus} --launcher pytorch  # train on distributed mode

# testing
mim test mmdet {config} --checkpoint {checkpont}  # test on single gpu
mim test mmdet {config} --checkpoint {checkpont} --gpus {num_gpus} --launcher pytorch  # test on distributed mode
```



## Results

| Detector                                                     | AP50   | APs    | APm    | APl    |
| ------------------------------------------------------------ | ------ | ------ | ------ | ------ |
| [YOLO v3 (darknet53, 320)](configs/yolov3/yolov3_d53_2xb32-320-273e_dior.py) | 55.8   | 9.2    | 42.7   | 81.1   |
| [YOLO v3 (darknet53, ms-608)](configs/yolov3/yolov3_d53_2xb4-ms-608-273e_dior.py) | 57.4   | 21.6   | 49.5   | 74.5   |
| [Faster RCNN (resnet50+fpn)](configs/faster_rcnn/faster-rcnn_r50_fpn_2xb8-30e_dior.py) | *54.8* | *18.5* | *45.3* | *75.5* |

