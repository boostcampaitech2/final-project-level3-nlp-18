import torch
from fairseq.models.transformer import TransformerModel

ko2je = TransformerModel.from_pretrained(
    'train/4k/ko-je/ckpt',
    checkpoint_file = 'checkpoint_best.pt',
    data_name_or_path = 'data/4k/ko-je-bin',
    bpe = 'sentencepiece',
    bpe_codes='train/4k/ko-je/ckpt/sentencepiece.bpe.model'
    
)
print(ko2je.translate('명절 때는 더 온다 세뱃돈 받을려고'))
