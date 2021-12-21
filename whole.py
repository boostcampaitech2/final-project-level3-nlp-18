import torch
from fairseq.models.transformer import TransformerModel

ko2je = TransformerModel.from_pretrained(
    'train/4k/ko-je/ckpt',
    checkpoint_file = 'checkpoint_best.pt',
    data_name_or_path = 'data/4k/ko-je-bin',
    bpe = 'subword_nmt',
    bep_codes = ?? (bpe에 관한 code파일인거 같은데?? 못 찾았어요)
    
)
ko2je.translate('안녕하세요. 반갑습니다')
.
