CUDA_VISIBLE_DEVICES=0,1,2,3 python -m torch.distributed.launch \
    --nproc_per_node=4 \
    --use_env main.py \
    --coco_path /home/u/woody8657/data/C426_Pneumothorax_preprocessed/Pix2Seq_data/ \
    --batch_size 2 \
    --pix2seq_lr \
    --large_scale_jitter \
    --rand_target $@ \
    