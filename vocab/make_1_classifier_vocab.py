#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 17:06:56 2017

@author: Takanori
"""

"""
最初の識別器に用いる辞書の作成
"""

import MeCab
from zodbpickle import pickle

f = open('dataset-txt/data.txt')
data1 = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

# 読み込んだテキストの分かち書き
m = MeCab.Tagger("-Owakati")
jlines = m.parse(data1)

# 空白で区切る
jlines = jlines.split(' ')

# 辞書の完成
# 重複したものを削除
jlines_uniq = list(set(jlines))
print(len(jlines_uniq))
print(type(jlines_uniq))

# 辞書の保存
pickle.dump(jlines_uniq, open('1_classifier_vocab.pkl','wb'), protocol=3 )










