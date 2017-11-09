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
result = re.search(pattern,response.text).group(1)

print(u"\n[translate.google.com] で翻訳") 
print(u"英語:"), 
print(origin)
print(u"日本語:"), 
print(result)

#soup = BeautifulSoup(response.text, "html.parser")
#list = soup.find_all("script")

#text = list[9].string
#words=text.split(";")
#print(words[13].encode("cp932"))

#count = 0
#for s in words:
#    try:
#        print(str(count)+"======================")
#        print(s.encode("cp932"))
#        count=count+1
#    except:
#        count=count+1
#        pass