import pandas as pd
import numpy as np
import codecs
import os
import re
import sentencepiece as spm
import argparse


sp = spm.SentencePieceProcessor()
###Gtext파일을 복원해서 평문으로 만들고 bpe.train에 붙이기 
def add_generated_sentence_je(sp, sents):
    #with codecs.open('jit/je.train', 'r', 'utf8') as jin : 
    #    print(len( jin.readlines() ))
    with codecs.open('jit/je.train', 'a', 'utf8') as jout:
        jout.write("\n".join("".join(sp.DecodePieces(sent)) for sent in sents))  
    #with codecs.open('jit/je.train', 'r', 'utf8') as jin : 
    #    print(len( jin.readlines() ))
    #jin.close()    
    jout.close()
    
def add_generated_sentence_ko(sp, sents):
    with codecs.open('jit/ko.train', 'a', 'utf8') as kout:
        kout.write("\n".join("".join(sp.DecodePieces(sent)) for sent in sents))  
    kout.close()
###결과 텍스트 파일을 de token화된 데이터만 있는 파일 Gtext파일로 만들기
if __name__ == '__main__' :   
    parser = argparse.ArgumentParser()
    parser.add_argument('--vocab_size', type=int, default=4000,
                        help="Total number of BPE tokens")
    parser.add_argument('--lang1', type=str, default= 'ko', help= "Source of language")
    parser.add_argument('--lang2', type=str, default='je', help="Target of language")
    hp = parser.parse_args()
    
    
    dir = 'data/{}k/bpe'.format(str(hp.vocab_size)[:-3])
    sp.Load(f"{dir}/bpe.model")
    list = []
    if hp.lang1 == 'ko' and hp.lang2 == 'je' : 
        with open('result/{}k/ko-je-bin/generate-test.txt'.format(str(hp.vocab_size)[:-3]), 'r', encoding='utf-8') as f :
            for line in f : 
                line_list = line.split()
                if line_list[0][0] == 'D' : 
                    list.append(line_list[2:])
        f.close()
        #print(len(list))
        add_generated_sentence_je(sp, list)
    else : 
        with open('result/{}k/je-ko-bin/generate-test.txt'.format(str(hp.vocab_size)[:-3]), 'r', encoding='utf-8') as f :
            for line in f : 
                line_list = line.split()
                if line_list[0][0] == 'D' : 
                    list.append(line_list[2:])
        f.close()
        add_generated_sentence_ko(sp,list)

        

'''
tgt = "판관헤난 거 ?"
src= "판관했던 거 ?"
token_src = sp.EncodeAsPieces(src)
token_tgt = sp.EncodeAsPieces(tgt)
decode = sp.DecodePieces(src.split())
decode_src = sp.DecodePieces(token_src)
decode_tgt = sp.DecodePieces(token_tgt)
print(decode)
print(token_src, token_tgt)
print(decode_src, decode_tgt)
'''