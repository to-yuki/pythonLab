# -*- coding: UTF-8 -*-
import requests
import re

from bs4 import BeautifulSoup
 
origin = 'Automate your work with Python.'
url = 'https://translate.google.com/?hl=ja#en/ja/'
response = requests.get(url, params={'q': origin})

# 受信データを全て表示する
#print(response.text)

# resopnse 内にある JavaScript コードから翻訳された
# 文字列を取得 TRANSLATED_TEXT='(翻訳されて文字列)'
pattern = r"TRANSLATED_TEXT='(.*?)'"
transValue = re.search(pattern,response.text).group(1)

print(u"\n[translate.google.com] で翻訳") 
print(u"英語:"), 
print(origin)
print(u"日本語:"), 
print(transValue)
