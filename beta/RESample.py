# -*- coding: UTF-8 -*-
import re

requestString = u"https://www.google.co.jp/search?hl=ja&source=hp&biw=&bih=&q=Python&btnG=Google+%E6%A4%9C%E7%B4%A2&gbv=1"

#match = re.search(u".*Python",requestString)

match = re.match(r"https://(.*)",requestString)

if match != None:
    print(type(match))
    #print(match.groups())
    print(match.group(1))

data = match.group(1)
match = re.match(r".*\?(.*)",data)

if match != None:
    print(type(match))
    #print(match.groups())
    print(match.group(1))

data2 = match.group(1)
list = data2.split("&")
print(list)

result = re.search(r"q=\'(.*?)\'",requestString).group(1)
print(result)