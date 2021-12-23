import numpy as np
import pandas as pd
import codecs
'''
with codecs.open('jit/ko.train','r','utf8') as f :
    with codecs.open('jit/je.train','r','utf8') as f1 :
        if len(f1.readlines()) == len(f.readlines()) : print('True')


with codecs.open('jit/ko.dev','r','utf8') as f :
    with codecs.open('jit/je.dev','r','utf8') as f1 :
        if len(f1.readlines()) == len(f.readlines()) : print('True')


with codecs.open('jit/ko.test','r','utf8') as f :
    with codecs.open('jit/je.test','r','utf8') as f1 :
        if len(f1.readlines()) == len(f.readlines()) : print('True')

'''
import random
from sklearn.model_selection import train_test_split
n = 0.2
m = 0.2
df = pd.read_csv('external.train')
df_train, df_test = train_test_split(df, test_size = 0.2, random_state =42 )
df_train, df_dev = train_test_split(df_train, test_size = 0.2, random_state =42 )
df_train = df_train.iloc[:]
df_dev = df_train.iloc[:]
df_test = df_train.iloc[:]
df_train.to_csv('jit/external.train',  index=False)
df_dev.to_csv('jit/external.dev',  index=False)
df_test.to_csv('jit/external.test', index=False)