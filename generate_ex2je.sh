
fairseq-interactive data/4k/ko-je-bin  \
  --input jit/external.train \
  --path train/4k/ko-je/ckpt/checkpoint_best.pt \
  --buffer-size 16 \
  --results-path result/4k/external-je-bin --beam 5 
