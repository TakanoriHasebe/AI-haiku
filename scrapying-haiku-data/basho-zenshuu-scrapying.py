#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 11:14:50 2017

@author: Takanori
"""

"""

今回、裁判データを得た方法でスクレイピングしたが、HTML全体構造を得ることはできなかった。
パーサーにはhtml.parser, lxml, html5libが存在していることに注意

このプログラムでは
http://www2.yamanashi-ken.ac.jp/~itoyo/basho/haikusyu/Default.htm
から芭蕉の俳句をスクレイピングし
.pklに保存している。

"""


# 必要なライブラリを記載
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import requests
import re
import codecs
from zodbpickle import pickle

# 芭蕉全集が入っているurl
html = urlopen('http://www2.yamanashi-ken.ac.jp/~itoyo/basho/haikusyu/Default.htm')

# web page全体のhtmlの構造が入っている
# parserにhtml.parserを指定
bsObj = BeautifulSoup(html, 'html.parser')

# htmlの全体構造の表示
# print(bsObj)

# htmlのaタグのみの抽出
# print(bsObj.find_all('a'))
basho_list = []
basho_list = bsObj.find_all('a')

# print(len(basho_list))
# print(basho_list[50])

temp_str = str(basho_list[50])
# print(temp_str)

# 俳句のみの取り出し
# print(re.sub(r'[a-z]*[<>.""/= ]', "", temp_str))

# Webページから俳句のみを取り出して、リストを作成
re_list_0 = []
for s in basho_list[50:]:
    
    re_list_0.append(re.sub(r'[a-z]*[#<>.""/= ]|[a-z]*[0123456789]*[#<>.""/= ]|[a-z]*[0123456789]*[#<>.""/= ]*[[0123456789]]', "", str(s)))
    
# 最初に作成した俳句を表示
# print(re_list_0)

# 配列の最初を表示
# print(re_list_0[0])

# 配列の最初の文字列の長さを表示
# print(len(re_list_0[0]))

# 俳句の配列から、必要な要素の抜き出し
re_list_1 = []
for i in range(0, len(re_list_0)):
    
    if len(re_list_0[i]) > 5:
        
        re_list_1.append(re_list_0[i])
        # print(i)
        # print(re_list_0[i])

# 上記のfor文で抜き出したものの表示
# print(re_list_1)

# 抜き出した俳句のリストから数字の削除
re_list_2 = []
for s in re_list_1:
    
    # print(re.sub(r'[0123456789]', "", str(s)))
    re_list_2.append(re.sub(r'[0123456789]', "", str(s)))

"""
# 芭蕉のリストをテキストで出力
f = open('temp.txt', 'w')
for sentence in re_list_2:
    f.write(str(sentence) + "\n")
f.close()
"""

# テキストの読み込み
fin = codecs.open('basho_haiku_list.txt', 'r', 'utf-8')
txtRaw = fin.read()
fin.close()

# 読み込んだテキストの表示
# print(txtRaw)
# print(type(txtRaw))

# 読み込んだテキストを配列に変換
basho_haiku_list = txtRaw.split('\n')
# print(len(basho_haiku_list))

# 配列に変換した芭蕉のリストを表示
# print(basho_haiku_list)

# 最後の配列を削除
del basho_haiku_list[-1]

# 表示
# print(basho_haiku_list)

# 作成した芭蕉のリストをpickle形式で保存
# pickle.dump(basho_haiku_list, open('basho_haiku_list.pkl','wb'), protocol=3 )










