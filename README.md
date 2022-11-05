# HBB Remote Sensing Object Detection

Horizontal object detection on remote sensing data sets with the new mmdetection.

Explore benchmark for comparison.

Personal maintenance and use.

### Support Dataset
- DIOR

### Support Model
- YOLOv3 (darknet53)

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