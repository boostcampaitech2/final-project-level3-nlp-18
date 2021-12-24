export lang1="je"
export lang2="ko"
fairseq-train data/4k/${lang1}-${lang2}-bin \
    --fp16 --arch transformer_align       \
    --optimizer adam \
    --lr 0.0005 \
    --label-smoothing 0.1 \
    --dropout 0.3       \
    --max-tokens 4000 \
    --lr-scheduler inverse_sqrt       \
    --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy       \
    --max-epoch 1 \
    --warmup-updates 4000 \
    --warmup-init-lr '1e-07'    \
    --adam-betas '(0.9, 0.98)'       \
    --save-dir train/4k/${lang1}-${lang2}/ckpt  \
    --save-interval 1
