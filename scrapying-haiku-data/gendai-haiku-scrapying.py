#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 13:26:07 2017

@author: Takanori
"""

"""

現代俳句データベースから俳句をスクレイピング

"""

# 必要なライブラリを記載
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
import requests
import re
import codecs
from zodbpickle import pickle

# url
# html = urlopen('')
html0 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E5%AE%87%E5%A4%9A%E5%96%9C%E4%BB%A3%E5%AD%90#result')
html1 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E5%92%8C%E7%9F%A5%E5%96%9C%E5%85%AB#result')
html2 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E9%88%B4%E6%9C%A8%E5%85%AD%E6%9E%97%E7%94%B7#result')
html3 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E5%8A%A0%E8%97%A4%E6%A5%B8%E9%82%A8#result')
html4 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E4%B8%AD%E6%9D%91%E8%8D%89%E7%94%B0%E7%94%B7#result')
html5 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E5%AE%AE%E5%9D%82%E9%9D%99%E7%94%9F#result')
html6 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=1&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html7 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=2&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html8 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=3&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html9 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=4&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html10 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=5&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html11 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=6&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html12 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=7&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html13 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=8&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html14 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=9&search_type=&author_name=%E9%87%91%E5%AD%90%E5%85%9C%E5%A4%AA&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html15 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E9%98%BF%E9%83%A8%E5%AE%8C%E5%B8%82#result')
html16 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=1&search_type=&author_name=%E9%98%BF%E9%83%A8%E5%AE%8C%E5%B8%82&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html17 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E6%BE%81%E8%B0%B7%E9%81%93#results')
html18 = urlopen('http://www.haiku-data.jp/author_work_list.php?next_i=1&search_type=&author_name=%E6%BE%81%E8%B0%B7%E9%81%93&database=%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E5%8D%94%E4%BC%9A%E3%80%8C%E7%8F%BE%E4%BB%A3%E4%BF%B3%E5%8F%A5%E3%83%87%E3%83%BC%E3%82%BF%E3%83%99%E3%83%BC%E3%82%B9%E3%80%8D&order=work_up#result')
html19 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E5%AF%BA%E7%94%B0%E4%BA%AC%E5%AD%90#result')
html20 = urlopen('http://www.haiku-data.jp/author_work_list.php?author_name=%E4%B8%89%E6%A9%8B%E6%95%8F%E9%9B%84#result')

# HTML
bsObj0 = BeautifulSoup(html0, 'html.parser')
bsObj1 = BeautifulSoup(html1, 'html.parser')
bsObj2 = BeautifulSoup(html2, 'html.parser')
bsObj3 = BeautifulSoup(html3, 'html.parser')
bsObj4 = BeautifulSoup(html4, 'html.parser')
bsObj5 = BeautifulSoup(html5, 'html.parser')
bsObj6 = BeautifulSoup(html6, 'html.parser')
bsObj7 = BeautifulSoup(html7, 'html.parser')
bsObj8 = BeautifulSoup(html8, 'html.parser')
bsObj9 = BeautifulSoup(html9, 'html.parser')
bsObj10 = BeautifulSoup(html10, 'html.parser')
bsObj11 = BeautifulSoup(html11, 'html.parser')
bsObj12 = BeautifulSoup(html12, 'html.parser')
bsObj13 = BeautifulSoup(html13, 'html.parser')
bsObj14 = BeautifulSoup(html14, 'html.parser')
bsObj15 = BeautifulSoup(html15, 'html.parser')
bsObj16 = BeautifulSoup(html16, 'html.parser')
bsObj17 = BeautifulSoup(html17, 'html.parser')
bsObj18 = BeautifulSoup(html18, 'html.parser')
bsObj19 = BeautifulSoup(html19, 'html.parser')
bsObj20 = BeautifulSoup(html20, 'html.parser')

# print(bsObj)

# 俳句を配列として抜き出し
haiku_list_0 = bsObj0.find_all('a')
haiku_list_1 = bsObj1.find_all('a')
haiku_list_2 = bsObj2.find_all('a')
haiku_list_3 = bsObj3.find_all('a')
haiku_list_4 = bsObj4.find_all('a')
haiku_list_5 = bsObj5.find_all('a')
haiku_list_6 = bsObj6.find_all('a') #
haiku_list_7 = bsObj7.find_all('a') #
haiku_list_8 = bsObj8.find_all('a') #
haiku_list_9 = bsObj9.find_all('a') #
haiku_list_10 = bsObj10.find_all('a') #
haiku_list_11 = bsObj11.find_all('a') #
haiku_list_12 = bsObj12.find_all('a') #
haiku_list_13 = bsObj13.find_all('a') #
haiku_list_14 = bsObj14.find_all('a') #
haiku_list_15 = bsObj15.find_all('a') 
haiku_list_16 = bsObj16.find_all('a') #
haiku_list_17 = bsObj17.find_all('a') 
haiku_list_18 = bsObj18.find_all('a') # 
haiku_list_19 = bsObj19.find_all('a') 
haiku_list_20 = bsObj20.find_all('a') 

# 俳句のみの表示
# print(haiku_list_0[4:-4])
# print(haiku_list_6[4:-5])

# いらない文字の削除
# print(haiku_list_0[4])
# temp = str(haiku_list_0[5])
# print(temp)
# print(re.sub(r'[a-z]', "", temp))
# print(re.sub(r'[ !-~]', "", temp))#半角記号,数字,英字

# 俳句のみを抜き出す関数
# 引数に、俳句のリスト、0 or 1を受け取る
def extract_haiku(moji, judge):
    
    # 最終的に返す配列
    extract_haiku_list = []
    
    # 俳句に関係した配列のみの抜き出し
    if judge == 0:
        mojiretu = moji[4:-4]
    else:
        mojiretu = moji[4:-5]
    
    # 配列から俳句のみを抜き出し
    for i in range(0, len(mojiretu)):
        
        # 空白, 半角記号, 数字, 英字の削除
        mojiretu[i] = re.sub(r'[ !-~]|\s', "", str(mojiretu[i]))
        extract_haiku_list.append(mojiretu[i])

    return extract_haiku_list

# temp = extract_haiku(haiku_list_0, 0)
# print(temp)
# print(len(temp))

# 今まで抜き出してきた俳句を追加する配列
haiku_list = []

# 関数を用いて俳句のみの抜き出し
haiku_list.extend(extract_haiku(haiku_list_0, 0))
haiku_list.extend(extract_haiku(haiku_list_1, 0))
haiku_list.extend(extract_haiku(haiku_list_2, 0))
haiku_list.extend(extract_haiku(haiku_list_3, 0))
haiku_list.extend(extract_haiku(haiku_list_4, 0))
haiku_list.extend(extract_haiku(haiku_list_5, 0))
haiku_list.extend(extract_haiku(haiku_list_6, 1))
haiku_list.extend(extract_haiku(haiku_list_7, 1))
haiku_list.extend(extract_haiku(haiku_list_8, 1))
haiku_list.extend(extract_haiku(haiku_list_9, 1))
haiku_list.extend(extract_haiku(haiku_list_10, 1))
haiku_list.extend(extract_haiku(haiku_list_11, 1))
haiku_list.extend(extract_haiku(haiku_list_12, 1))
haiku_list.extend(extract_haiku(haiku_list_13, 1))
haiku_list.extend(extract_haiku(haiku_list_14, 1))
haiku_list.extend(extract_haiku(haiku_list_15, 0))
haiku_list.extend(extract_haiku(haiku_list_16, 1))
haiku_list.extend(extract_haiku(haiku_list_17, 0))
haiku_list.extend(extract_haiku(haiku_list_18, 1))
haiku_list.extend(extract_haiku(haiku_list_19, 0))
haiku_list.extend(extract_haiku(haiku_list_20, 0))

# 抜き出した俳句の表示
# print(haiku_list)
print(len(haiku_list))

# 現代俳句のリストをテキストで出力
f = open('gendai_haiku_list.txt', 'w')
for sentence in haiku_list:
    f.write(str(sentence) + "\n")
f.close()

# 現代俳句のテキストの読み込み
fin = codecs.open('gendai_haiku_list.txt', 'r', 'utf-8')
txtRaw = fin.read()
fin.close()

# 読み込んだ現代俳句をリストに変換
gendai_haiku_list = txtRaw.split('\n')

# 最後の配列を削除
del gendai_haiku_list[-1]

# 作成した現代俳句のリストをpickle形式で保存
pickle.dump(gendai_haiku_list, open('gendai_haiku_list.pkl','wb'), protocol=3 )


