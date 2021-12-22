import os
import sentencepiece as spm
import pandas as pd
import argparse
import numpy as np
import codecs

if __name__ == "__main__":
    # arguments setting
    parser = argparse.ArgumentParser()
    parser.add_argument('--jit', type=str, required=True,
                        help="JIT directory path")
    hp = parser.parse_args()

    # train/valid/test
    train_je = codecs.open(f"{hp.jit}/je.train", 'r', 'utf8').read().splitlines()
    dev_je = codecs.open(f"{hp.jit}/je.dev", 'r', 'utf8').read().splitlines()
    test_je = codecs.open(f"{hp.jit}/je.test", 'r', 'utf8').read().splitlines()
    train_ko = codecs.open(f"{hp.jit}/ko.train", 'r', 'utf8').read().splitlines()
    dev_ko = codecs.open(f"{hp.jit}/ko.dev", 'r', 'utf8').read().splitlines()
    test_ko = codecs.open(f"{hp.jit}/ko.test", 'r', 'utf8').read().splitlines()
    
    train_ko = pd.DataFrame(train_ko + dev_ko, columns=["표준어"])
    train_je = pd.DataFrame(train_je + dev_je, columns=["제주어"])
    test_ko = pd.DataFrame(test_ko, columns=["표준어"])
    test_je = pd.DataFrame(test_je, columns=["제주어"])
    
    train = [train_ko, train_je]
    test = [test_ko, test_je]
    
    train_csv = pd.concat(train, axis=1)
    test_csv = pd.concat(test, axis=1)
    
    jit_train = pd.DataFrame(train_csv)
    jit_train.to_csv('jit_train.csv',index=False, encoding='utf-8-sig')
    jit_test = pd.DataFrame(test_csv)
    jit_test.to_csv('jit_test.csv',index=False, encoding='utf-8-sig')
    
    
    train_v2 = "train_v2.csv"
    hub_train = pd.read_csv(train_v2)
    
    
    tot = [jit_train, hub_train]
    tot_train = pd.concat(tot)
    print(np.shape(jit_train))
    print(np.shape(hub_train))
    print(np.shape(tot_train))
    tot_train.to_csv('tot_train.csv', index=False, encoding="utf-8-sig")
    
    '''
    tot_test = pd.concat([jit_test, hub_test])
    print(np.shape(jit_test))
    ptint(np.shape(hub_test))
    print(np.shape(tot_test))
    tot_test.to_csv('tot_test.csv', index=False, encoding='utf-8-sig')
    '''
   
    



