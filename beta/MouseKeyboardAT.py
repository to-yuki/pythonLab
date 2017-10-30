# coding: UTF-8
# pylint: disable=invalid-name

import pyautogui as gui
import time

# Windowsサイズの取得
w,h = gui.size()
print("Windows Size : " + str(w) + " x " + str(h))

 # 現在のマウスポジションの取得
x,y = gui.position()
print("Current x,y : " + str(x) + "," + str(y))

# スクリーン範囲の確認
check = gui.onScreen(100,100)
#check = gui.onScreen(2000,3000)
if check:
    print("x=100,y=100 " + "onScreen")
else:
    print("x=2000,y=3000 " + "off onScreen")

# マウスカーソルの中央への移動
gui.moveTo(x=960,y=540)
x,y = gui.position()
print("Point after moving x,y : " + str(x) + "," + str(y))

# AlartBoxの表示
gui.confirm(text="電卓アプリを最少サイズで開き画面に表示出来ましたか？", title="確認！",buttons=['OK', 'Cancel'])

# 指定される画像をスクリーンから検出する
try:
    x,y,width,height = gui.locateOnScreen('c.png', grayscale=True)
    print("c.png: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
    gui.click(x=x+5,y=y+5) 
    x,y,width,height = gui.locateOnScreen('2.png', grayscale=True)
    print("2.png: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
    gui.click(x=x+5,y=y+5) 
    x,y,width,height = gui.locateOnScreen('x.png', grayscale=True)
    print("x.png: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
    gui.click(x=x+5,y=y+5)
    x,y,width,height = gui.locateOnScreen('2.png', grayscale=True)
    print("2.png: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
    gui.click(x=x+5,y=y+5)
    x,y,width,height = gui.locateOnScreen('equal.png', grayscale=True)
    print("equal.png: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
    gui.click(x=x+5,y=y+5)
except:
    print("Image does not match")
