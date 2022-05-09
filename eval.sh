python -m torch.distributed.launch \
     --nproc_per_node 2 \
     --use_env main.py \
     --coco_path /home/u/woody8657/data/C426_Pneumothorax_preprocessed/Pix2Seq_data/ \
     --batch_size 4 \
     --eval \
     --resume /home/u/woody8657/projs/Pneumothorax-detection/Stable-Pix2Seq/output/checkpoint.pth