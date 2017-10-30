# coding: UTF-8
# pylint: disable=invalid-name
import codecs
import ssl
import urllib2

from bs4 import BeautifulSoup

# SSL自己証明書のエラー無効化
ssl._create_default_https_context = ssl._create_unverified_context

#
# python Coding UTF-8(powershell [chcp 65001] Settings) 
#
def cp65001(name):
    if name.lower() == 'cp65001':
        return codecs.lookup('utf-8')
    
codecs.register(cp65001)

# アクセスするURL
#url = "http://www.nikkei.com/"
url = "https://192.168.200.225/api/2.0/vdn/controller"
user = "admin"
password = "VMware1!"
headers = {}
headers["authorization"] = "Basic " + (user + ":" + password).encode("base64")[:-1]
req = urllib2.Request(url=url, headers=headers)

# URLにアクセスする htmlが帰ってくる
html = urllib2.urlopen(req)

#print(html.read())

# URLにアクセスする htmlが帰ってくる
#html = urllib2.urlopen(url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html, "html.parser")

# version要素を取得する
version_tag = soup.find("version")

# 要素の文字列を取得する
version = version_tag.string

# ipAddress 要素を取得する
ip_tag_list = soup.find_all("ipaddress")

# 要素値を出力
print 'Version : ',
print version

print 'ipaddress : '
for ip_tag in ip_tag_list:
    print '\t' + ip_tag.string

# 全てのレスポンスデータ表示
#print '==[Response Data]=='
#print soup
