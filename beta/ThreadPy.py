# -*- coding: UTF-8 -*-
import threading
from time import sleep

# スレッド化する関数1
def thread1():
    # 1秒間隔で "T1" を表示
    for i in range(5):
        sleep(1)
        print "T1 ",

# スレッド化する関数2
def thread2():
    # 2秒間隔で "T2" を表示
    for i in range(5):
        sleep(2)
        print "T2 ",

# メインスレッド関数
def mainThread():
    # スレッドオブジェクトの作成
    t1 = threading.Thread(target=thread1)
    t2 = threading.Thread(target=thread2)

    # 作成したスレッドオブジェクトのスタート
    t1.start()
    t2.start()

# メインスレッド関数を呼び出し
if __name__=='__main__':
    mainThread()