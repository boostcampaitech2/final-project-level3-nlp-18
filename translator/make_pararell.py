import pandas as pd
import numpy as np
import codecs

def add_generated_sentence_je(sents):
    with codecs.open('jit/je.train', 'a', 'utf8') as jout:
        jout.write("\n".join(" ".join(sent) for sent in sents))
        
def add_generated_sentence_ko(sents):
    with codecs.open('jit/ko.train', 'a', 'utf8') as jout:
        jout.write("\n".join(" ".join(sent) for sent in sents))    
        
if __name__ == '__main__' :   
    
    list_ko, list_je = [], []
    with open('backtranslation_output.txt', 'r', encoding='utf-8') as f :
        for line in f : 
            line_list = line.split()
            if line_list[0][0] == '제' : 
                list_je.append(line_list[2:])
            if line_list[0][0] == '표' :
                list_ko.append(line_list[2:])
    add_generated_sentence_je(list_je)
    add_generated_sentence_ko(list_ko)
