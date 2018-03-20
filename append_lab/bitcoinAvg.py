# coding: UTF-8
import requests
import json
from time import sleep
import datetime
import locale

locale.setlocale(locale.LC_ALL,"Japanese")

# coin List
coins = [[1,'BTC','btc_jpy'],[2,'XEM','xem_jpy'],[3,'MONA','mona_jpy']]
# Zaif
url = 'https://api.zaif.jp/api/1/last_price/'

try:
    while True:
        print(datetime.datetime.today().strftime("%x %X"))
        for i in range(len(coins)):
            response = requests.get(url+coins[i][2])
            if response.status_code != 200:
                raise Exception('return status code is {}'.format(response.status_code))

            # Responseデータの表示
            #print(response.text)
            rate = json.loads(response.text)
            print(u"\t%-4s : ￥%-10s"% (coins[i][1], rate['last_price']))
        sleep(60)
except KeyboardInterrupt:
    print(u"Ctr+C割り込みによる終了")
