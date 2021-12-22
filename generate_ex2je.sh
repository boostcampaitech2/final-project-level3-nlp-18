export lang1="external"
export lang2="je"

fairseq-interactive data/4k/${lang1}-${lang2}-bin  \
  --input jit/test.train \
  --path train/4k/ko-je/ckpt/checkpoint_best.pt \
  --buffer-size 16 \
  --results-path result/4k/${lang1}-${lang2}-bin --beam 5 > backtranslation_output.txt
