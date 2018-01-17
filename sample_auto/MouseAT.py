# -*- coding: UTF-8 -*-
# pylint: disable=invalid-name

import pyautogui as gui
from pywinauto import application
import time

# Windowsサイズの取得
w,h = gui.size()
print("Windows Size : " + str(w) + " x " + str(h))

 # 現在のマウスポジションの取得
x,y = gui.position()
print("Current x,y : " + str(x) + "," + str(y))

# Paintアプリケーションに描画する
mspaint = application.Application()
mspaint.start("mspaint.exe")
select = gui.confirm(text="ペイントアプリを画面中央表示して、\n直線を選択してください。", title="確認！",buttons=['OK', 'Cancel'])
if select in "OK":
    # マウスカーソルの中央への移動
    gui.moveTo(x=(w/2),y=(h/2))
    x,y = gui.position()
    print("Point after moving x,y : " + str(x) + "," + str(y))
    gui.dragTo(x=(x/2)+100,y=(y/2)+100,button='left')
    # gui.mouseDown(button='left')
    # gui.mouseUp(button='left',x=(x/2)+100,y=(y/2)+100)

# スクリーン範囲の確認
check = gui.onScreen(100,100)
#check = gui.onScreen(2000,3000)
if check:
    print("x=100,y=100 " + "onScreen")
else:
    print("x=2000,y=3000 " + "off onScreen")

# 電卓で計算する
calc = application.Application()
calc.start("calc.exe")
select = gui.confirm(text="電卓アプリを最小画面で表示してください。", title="確認！",buttons=['OK', 'Cancel'])
if select in "OK":
    # 指定される画像をスクリーンから検出する
    try:
        x,y,width,height = gui.locateOnScreen('c.png', grayscale=True)
        print("c.png Found!: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
        gui.click(x=x+5,y=y+5) 
        x,y,width,height = gui.locateOnScreen('2.png', grayscale=True)
        print("2.png Found!: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
        gui.click(x=x+5,y=y+5) 
        x,y,width,height = gui.locateOnScreen('x.png', grayscale=True)
        print("x.png Found!: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
        gui.click(x=x+5,y=y+5)
        x,y,width,height = gui.locateOnScreen('9.png', grayscale=True)
        print("9.png Found!: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
        gui.click(x=x+5,y=y+5)
        x,y,width,height = gui.locateOnScreen('equal.png', grayscale=True)
        print("equal.png Found!: x=" + str(x) + ",y=" + str(y) + ",width=" + str(width) + ",height=" + str(height))
        gui.click(x=x+5,y=y+5)
    except:
        print("Image does not match")
else:
    pass
gui.alert(text="処理終了",title="確認！",button="OK")