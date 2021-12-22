import pandas as pd
import numpy as np
import codecs
import sentencepiece as spm
import argparse

sp = spm.SentencePieceProcessor()
def add_generated_sentence(sp, sents):
    with codecs.open('Gtext_je', 'w', 'utf8') as jout:
        jout.write("\n".join("".join(sp.DecodePieces(sent)) for sent in sents))  

if __name__ == '__main__' :   
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_size', type=int, default=4000,
                        help="Total number of BPE tokens")
    parser.add_argument('--lang1', type=str, default= 'external', help= "Exteranl Source of language")
    parser.add_argument('--lang2', type=str, default='je', help="Target of language")
    hp = parser.parse_args()
    
    dir = 'data/{}k/bpe'.format(str(hp.vocab_size)[:-3])
    sp.Load(f"{dir}/bpe.model")
    list = []
    with open('result/{}k/external-je-bin/generate-test.txt'.format(str(hp.vocab_size)[:-3]), 'r', encoding='utf-8') as f :
        for line in f : 
            line_list = line.split()
            if line_list[0][0] == 'D' : 
                list.append(line_list[2:])
    add_generated_sentence(sp, list)
