import pandas as pd
import numpy as np
import codecs


def add_generated_sentence(sents):
    with codecs.open('Gtext_je', 'w', 'utf8') as jout:
        jout.write("\n".join(" ".join(sent) for sent in sents))  

if __name__ == '__main__' :   
    
    list = []
    with open('backtranslation_output.txt', 'r', encoding='utf-8') as f :
        for line in f : 
            line_list = line.split()

            if line_list[0][0] == 'D' : 
                list.append(line_list[2:])
    add_generated_sentence(list)
