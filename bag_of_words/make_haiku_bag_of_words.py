#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:29:54 2017

@author: Takanori
"""

"""

bag-of-wordsを作成する

"""
from zodbpickle import pickle
import codecs
import MeCab
import os
import glob
from collections import OrderedDict
import pickle

with open('../vocab/haiku-vocab-0.pkl', 'rb')\
     as f: vocab = pickle.Unpickler(f).load()

# 分かち書き
m = MeCab.Tagger("-Owakati")

# bag of wordsを作成する関数
bag_of_words = []

# テキストの読み込み
fin = codecs.open('../basho-haiku-data/basho_haiku_list.txt', 'r', 'utf-8')
txtRaw = fin.read()
fin.close()

# 読み込んだ現代俳句をリストに変換
gendai_haiku_list = txtRaw.split('\n')
# print(len(gendai_haiku_list))

# 簡単な文章に対して、辞書を用いてbag_of_wordsを作成
temp_list = gendai_haiku_list[:2]
# print(temp_list)

# 俳句を分かち書き
wakati_haiku = []
for s in temp_list:
    
    wakati_haiku.append(m.parse(s).replace(' \n', '').split(' '))
print(wakati_haiku)  

for i in range(0, len(wakati_haiku)):
    # 一文字づつ見て、辞書に出現回数を追加
    for s in wakati_haiku[i]:
        
        # print(s)
        vocab[s] += 1
    
    # bag_of_wordsの作成
    bag_of_words.append(list(vocab.values()))
    
    # vocabを初期化
    for s in vocab:
        vocab[s] = 0
        
    # print('')




