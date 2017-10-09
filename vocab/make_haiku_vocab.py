#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:05:24 2017

@author: Takanori
"""

"""

芭蕉と現代俳句から辞書を作成する
dicdir =  @prefix@/lib/mecab/dic/ipadic

"""

import MeCab
from zodbpickle import pickle

f = open('haiku-vocab-0.txt')
data = f.read()  # ファイル終端まで全て読んだデータを返す
f.close()

"""
def make_vocab(data):
    
    # 読み込んだテキストの分かち書き
    m = MeCab.Tagger("-Owakati")
    jlines = m.parse(data)
    
    # 空白で区切る
    jlines = jlines.split(' ')
    
    
    # 辞書の完成
    jlines_uniq = list(set(jlines)) # 重複したものを削除
    print(len(jlines_uniq))
    print(type(jlines_uniq))
    
    # 辞書の保存
    pickle.dump(jlines_uniq, open('haiku-vocab-0.pkl','wb'), protocol=3 )
    
    return jlines_uniq
   

vocab = make_vocab(data)
print(vocab)
""" 

# 読み込んだテキストの分かち書き
m = MeCab.Tagger("-Owakati")
jlines = m.parse(data)

# 空白で区切る
jlines = jlines.split(' ')

# 辞書の完成
# 重複したものを削除
jlines_uniq = set(jlines)
print(len(jlines_uniq))
print(type(jlines_uniq))
list(jlines)


"""
bag_of_wordsを作成する辞書を作成
OrderedDictを用いる
"""


# 辞書の保存
# pickle.dump(jlines_uniq, open('haiku-vocab-0.pkl','wb'), protocol=3 )







