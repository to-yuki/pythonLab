# -*- coding: UTF-8 -*-
import requests
import re

from bs4 import BeautifulSoup
 
origin = 'Automate your work with Python.'
url = 'https://translate.google.com/?hl=ja#en/ja/'
response = requests.get(url, params={'q': origin})

#print(r.text)

pattern = "TRANSLATED_TEXT=\'(.*?)\'"
result = re.search(pattern,response.text).group(1)

print(u"[translate.google.com] で翻訳") 
print(u"英語:"), 
print(origin)
print(u"日本語:"), 
print(result)
