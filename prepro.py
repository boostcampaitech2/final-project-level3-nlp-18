import os
import argparse

def prepro(src, tgt, vocab_size):
    dir = "data/{}k".format(str(vocab_size)[:-3])
    destdir = f"{dir}/{src}-{tgt}-bin"
    if src == 'external' : 
        trainpref = f'{dir}/bpe_ex/train'
        prepro = f"fairseq-preprocess \
                    --source-lang {src} \
                    --target-lang {tgt} \
                    --trainpref {trainpref} \
                    --validpref {dir}/bpe_ex/dev \
                    --testpref {dir}/bpe_ex/test \
                    --srcdict {dir}/bpe_ex/bpe.dict \
                    --tgtdict {dir}/bpe_ex/bpe.dict \
                    --workers 8 \
                    --destdir {destdir}"
    else :       
            trainpref = f"{dir}/bpe/train"
            prepro = f"fairseq-preprocess \
                --source-lang {src} \
                --target-lang {tgt} \
                --trainpref {trainpref} \
                --validpref {dir}/bpe/dev \
                --testpref {dir}/bpe/test \
                --srcdict {dir}/bpe/bpe.dict \
                --tgtdict {dir}/bpe/bpe.dict \
                --workers 8 \
                --destdir {destdir}"                                                    
    os.system(prepro)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, required=True,
                        help="source language. je or ko")
    parser.add_argument('--tgt', type=str, required=True,
                        help="target language. je or ko")
    parser.add_argument('--vocab_size', type=int, default=8000,
                        help='Total number of BPE tokens')
    hp = parser.parse_args()

    prepro(hp.src, hp.tgt, hp.vocab_size)

