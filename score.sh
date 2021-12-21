##미완성 파일, Generate가 잘 작동하면 필요없을지도 모른다

export lang1='ko'
export lang2='je'

fairseq-score data/4k/${lang1}-${lang2}-bin  \
  --path train/4k/${lang1}-${lang2}/ckpt/checkpoint_best.pt \
