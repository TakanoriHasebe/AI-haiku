#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:46:45 2017

@author: Takanori
"""

"""
Bag of Wordsの作成
"""

from zodbpickle import pickle
import codecs
import MeCab
import os
import glob
from collections import OrderedDict
import pickle

with open('1_classifier_vocab.pkl', 'rb')\
     as f: vocab = pickle.Unpickler(f).load()

# ファイル内のテキストを全て読み込み
files = os.listdir('dataset-txt/')
print(len(files[1:]))

bag_of_words = list()
# Bag of Wordsを作成するテキストの読み込み
for t in files[1:]:
    
    # テキストの読み込み
    fin = codecs.open('dataset-txt/'+str(t), 'r', 'utf-8')
    data1 = fin.read()
    fin.close()
    
    # 分かち書き
    m = MeCab.Tagger("-Owakati")
    jlines = m.parse(data1)
    
    # 空白で分割
    jlines_wakati = jlines.split(' ')
    # print(len(jlines_wakati))
    # print(jlines_wakati)
    
    # Bag of Wordsの作成
    for w in jlines_wakati:
        vocab[w] += 1
    
    bag_of_words.append(list(vocab.values()))
    
    for w in vocab:
        vocab[w] = 0
 

print(len(bag_of_words))
pickle.dump(bag_of_words, open('1_classifier_bag_of_words.pkl','wb'), protocol=3)







