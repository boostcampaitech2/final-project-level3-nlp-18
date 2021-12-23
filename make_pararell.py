import pandas as pd
import numpy as np
import codecs

def add_generated_sentence(sents):
    with codecs.open('jit/je.train', 'a', 'utf8') as jout:
        jout.write("\n".join(" ".join(sent) for sent in sents))  
        
if __name__ == '__main__' :   
    
    list = []
    with open('backtranslation_output.txt', 'r', encoding='utf-8') as f :
        for line in f : 
            line_list = line.split()
            if line_list[0][0] == '제' : 
                list.append(line_list[2:])
    add_generated_sentence(list)
    
    train_ko_ex = codecs.open("jit/external.train", 'r', 'utf8').read().splitlines()
    dev_ko_ex = codecs.open("jit/external.dev", 'r', 'utf8').read().splitlines()
    test_ko_ex = codecs.open("jit/external.test", 'r', 'utf8').read().splitlines()
    train_ko = codecs.open("jit/ko.train", 'r', 'utf8').read().splitlines()
    
    with codecs.open("jit/ko.train", 'a', 'utf8') as fout:
        fout.write("\n".join(train_ko_ex + dev_ko_ex + test_ko_ex))
            

            
            


