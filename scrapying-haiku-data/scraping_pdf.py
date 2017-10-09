#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 15:04:25 2016
@author: takanori.hasebe
"""

"""
このプログラムは
指定したa href='...'
の...の部分をとってくるプログラム
つまり判例のpdfのurlをダウンロードしてくる
プログラムをここでは書いている
"""

from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen

#家庭的
#html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeGengoFrom%5D=&filter%5BjudgeYearFrom%5D=&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=&filter%5BjudgeYearTo%5D=&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E5%AE%B6%E5%BA%AD%E7%9A%84&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
#運転
#html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list5?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeGengoFrom%5D=&filter%5BjudgeYearFrom%5D=&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=&filter%5BjudgeYearTo%5D=&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5BjikenName%5D=&filter%5Btext1%5D=%E9%81%8B%E8%BB%A2&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
#人工知能
#html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?action_search=%E6%A4%9C%E7%B4%A2&filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeGengoFrom%5D=&filter%5BjudgeYearFrom%5D=&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=&filter%5BjudgeYearTo%5D=&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E4%BA%BA%E5%B7%A5%E7%9F%A5%E8%83%BD&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=&filter%5Btext8%5D=&filter%5Btext9%5D=')
#交通
# html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?page=351&sort=1&filter%5Btext1%5D=%E4%BA%A4%E9%80%9A')
# 交通事故かつ損害賠償
# html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?page=1&sort=1&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext4%5D=%E8%B3%A0%E5%84%9F%E8%AB%8B%E6%B1%82&filter%5Btext7%5D=%E4%BA%A4%E9%80%9A%E4%BA%8B%E6%95%85')

# url = 'http://www.courts.go.jp/app/hanrei_jp/list1?page=1&sort=1&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext4%5D=%E8%B3%A0%E5%84%9F%E8%AB%8B%E6%B1%82&filter%5Btext7%5D=%E4%BA%A4%E9%80%9A%E4%BA%8B%E6%95%85'
# 懲役
# html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E6%87%B2%E5%BD%B9&filter%5Btext5%5D=%E7%A6%81%E9%8C%AE&filter%5Btext6%5D=%E7%95%99%E7%BD%AE&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
# url = 'http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E6%87%B2%E5%BD%B9&filter%5Btext5%5D=%E7%A6%81%E9%8C%AE&filter%5Btext6%5D=%E7%95%99%E7%BD%AE&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2'

# 猶予
# html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E7%8C%B6%E4%BA%88&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
# url = 'http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E7%8C%B6%E4%BA%88&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2'

# 損害賠償
# html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F%E8%AB%8B%E6%B1%82&filter%5Btext5%5D=%E6%94%AF%E6%89%95%E3%81%88&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
# url = 'http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E6%90%8D%E5%AE%B3%E8%B3%A0%E5%84%9F%E8%AB%8B%E6%B1%82&filter%5Btext5%5D=%E6%94%AF%E6%89%95%E3%81%88&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2'

# 無罪
html = urlopen('http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E8%A2%AB%E5%91%8A%E4%BA%BA%E3%81%AF%E7%84%A1%E7%BD%AA&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2')
url = 'http://www.courts.go.jp/app/hanrei_jp/list1?filter%5BcourtName%5D=&filter%5BcourtType%5D=&filter%5BbranchName%5D=&filter%5BjikenGengo%5D=&filter%5BjikenYear%5D=&filter%5BjikenCode%5D=&filter%5BjikenNumber%5D=&filter%5BjudgeDateMode%5D=2&filter%5BjudgeGengoFrom%5D=%E6%98%AD%E5%92%8C&filter%5BjudgeYearFrom%5D=40&filter%5BjudgeMonthFrom%5D=&filter%5BjudgeDayFrom%5D=&filter%5BjudgeGengoTo%5D=%E5%B9%B3%E6%88%90&filter%5BjudgeYearTo%5D=30&filter%5BjudgeMonthTo%5D=&filter%5BjudgeDayTo%5D=&filter%5Btext1%5D=%E9%81%93%E8%B7%AF%E4%BA%A4%E9%80%9A%E6%B3%95&filter%5Btext2%5D=&filter%5Btext3%5D=&filter%5Btext4%5D=%E8%A2%AB%E5%91%8A%E4%BA%BA%E3%81%AF%E7%84%A1%E7%BD%AA&filter%5Btext5%5D=&filter%5Btext6%5D=&filter%5Btext7%5D=%E6%99%82%E9%80%9F&filter%5Btext8%5D=&filter%5Btext9%5D=&action_search=%E6%A4%9C%E7%B4%A2'
cnt = 0
n = 0

#最後のページまで
while True:
    
    print(str(n + 1)+'ページ目')
    print(url)
    
    #web page全体のhtmlの構造が入っている
    bsObj = BeautifulSoup(html.read(), 'lxml')
    
    #web page全体から一番最初の<a href=''>を取得
    result = bsObj.a['href']
    
    #web page全体の全ての<a href=''>を取得
    bsObj.find_all('a')  # aタグ全てを取得。リストで返ってくる
    
    #結果をリスト形式で保存する
    hrefResult = list()
    for link in bsObj.find_all('a'):
        
        #print(link.get('href'))   # 全てのリンク先を表示
        hrefResult.append(link.get('href'))
    
    #pdfをダウンロードするリンクを抽出
    result = list()    
    for i in range(len(hrefResult)):
        
        if hrefResult[i] == None:
            
            pass
        elif '/app/files' in hrefResult[i]:
            
            #print(i)
            result.append(hrefResult[i])
        
    #print('len(result): '+str(len(result)))
    #print(result)
    
    #len(result)
    #ここでurlで指定さてた判例データのpdfをとってきている
    topStr = 'http://www.courts.go.jp/'
    for i in range(len(result)):
        
        print('cnt: '+str(cnt))
        url = topStr + result[i]
        #print(url)
        urllib.request.urlretrieve(url, 'notguilty/notguilty'+str(cnt)+'.pdf')
        cnt += 1
    
    
    topStr = 'http://www.courts.go.jp'
    
    print('cnt:: '+str(cnt))
    
    """""""""""""""""""""""""""""""""""
    ###ここでダウンロードしたい件数を必ず指定する
    """""""""""""""""""""""""""""""""""
    if cnt == int(35): 
        
        break
        
    elif '/app/hanrei_jp/list1' in hrefResult[-3]:
        
        url = topStr + hrefResult[-3]
        #print(url) 
    
    elif '/app/hanrei_jp/list5' in hrefResult[-3]:
        
        url = topStr + hrefResult[-3]
        #print(url)    
    elif '/app/hanrei_jp/list0' in hrefResult[-3]:
        
        url = topStr + hrefResult[-3]
        #print(url)    
    
    else:
        
        break    
        
    html = urlopen(url)
    n += 1

print('クローリング終了')
