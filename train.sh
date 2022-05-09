#!/bin/bash
python -m torch.distributed.launch \
    --nproc_per_node=4 \
    --use_env main.py \
    --coco_path ./coco \
    --epochs 60 \
    --lr 0.00003 \
    --eval_epoch 1 \
    --batch_size 1 \
    --pix2seq_lr \
    --large_scale_jitter \
    --rand_target $@ \
    --resume /home/u/woody8657/projs/Pneumothorax-detection/Pretrained-Pix2Seq/weights/checkpoint_e299_ap370.pth \
    --model pix2seq \
    --output_dir ./output_lr3e-5_e60