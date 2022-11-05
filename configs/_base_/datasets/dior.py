# Modified on coco_detection.py of mmdetection, 2022/11/01.

# dataset settings
dataset_type = 'CocoDataset'
data_root = 'data/DIOR/'
metainfo = {
    'CLASSES':
    ('airplane', 'airport', 'baseball field', 'basketball court', 'bridge',
     'chimney', 'dam', 'expressway service area', 'expressway toll station',
     'golf field', 'ground track field', 'harbor', 'overpass', 'ship',
     'stadium', 'storage tank', 'tennis court', 'train station', 'vehicle',
     'windmill')}
file_client_args = dict(backend='disk')
train_pipeline = [
    dict(type='LoadImageFromFile', file_client_args=file_client_args),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
test_pipeline = [
    dict(type='LoadImageFromFile', file_client_args=file_client_args),
    dict(type='Resize', scale=(1333, 800), keep_ratio=True),
    # If you don't have a gt annotation, delete the pipeline
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PackDetInputs',
        meta_keys=('img_id', 'img_path', 'ori_shape', 'img_shape',
                   'scale_factor'))
]
train_dataloader = dict(
    batch_size=4,
    num_workers=2,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    batch_sampler=dict(type='AspectRatioBatchSampler'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        metainfo=metainfo,
        ann_file='coco_ann/DIOR_train_coco.json',
        data_prefix=dict(img='JPEGImages-trainval/'),
        filter_cfg=dict(filter_empty_gt=True, min_size=32),  # TODO
        pipeline=train_pipeline))
val_dataloader = dict(
    batch_size=4,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        metainfo=metainfo,
        ann_file='coco_ann/DIOR_val_coco.json',
        data_prefix=dict(img='JPEGImages-trainval/'),
        test_mode=True,
        pipeline=test_pipeline))
test_dataloader = dict(
    batch_size=4,
    num_workers=2,
    persistent_workers=True,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        metainfo=metainfo,
        ann_file='coco_ann/DIOR_test_coco.json',
        data_prefix=dict(img='JPEGImages-test/'),
        test_mode=True,
        pipeline=test_pipeline))

val_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'coco_ann/DIOR_val_coco.json',
    metric='bbox',
    format_only=False,
    iou_thrs=[0.5],
    classwise=True)
test_evaluator = dict(
    type='CocoMetric',
    ann_file=data_root + 'coco_ann/DIOR_test_coco.json',
    metric='bbox',
    format_only=False,
    iou_thrs=[0.5],
    classwise=True)

# inference on test dataset and
# format the output results for submission.
# test_dataloader = dict(
#     batch_size=1,
#     num_workers=2,
#     persistent_workers=True,
#     drop_last=False,
#     sampler=dict(type='DefaultSampler', shuffle=False),
#     dataset=dict(
#         type=dataset_type,
#         data_root=data_root,
#         ann_file=data_root + 'annotations/image_info_test-dev2017.json',
#         data_prefix=dict(img='test2017/'),
#         test_mode=True,
#         pipeline=test_pipeline))
# test_evaluator = dict(
#     type='CocoMetric',
#     metric='bbox',
#     format_only=True,
#     ann_file=data_root + 'annotations/image_info_test-dev2017.json',
#     outfile_prefix='./work_dirs/coco_detection/test')
