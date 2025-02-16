_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/dior-trainval.py',
    '../_base_/schedules/schedule_30e.py', '../_base_/default_runtime.py'
]

model = dict(roi_head=dict(bbox_head=dict(num_classes=20)))

batch_size = 8
train_dataloader = dict(
    batch_size=batch_size)
val_dataloader = dict(
    batch_size=batch_size)
test_dataloader = dict(
    batch_size=batch_size)

default_hooks = dict(checkpoint=dict(type='CheckpointHook', interval=10))

auto_scale_lr = dict(enable=True)
