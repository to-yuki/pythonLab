# coding: UTF-8
# pylint: disable=invalid-name

import pyautogui as gui
import time

w,h = gui.size()
print "Windows Size : " + str(w) + " " + str(h)

i = 200

while i < 1000:
    gui.moveTo(x=i,y=i)
    mouseX,mouseY = gui.position()
    print "Mouse X:" + str(mouseX) + " MouseY:" + str(mouseY)
    i +=1
