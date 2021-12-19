export lang1="ko"
export lang2="je"

fairseq-interactive data/4k/${lang1}-${lang2}-bin  \
  --path train/4k/${lang1}-${lang2}/ckpt/checkpoint_best.pt \
  --beam 5 