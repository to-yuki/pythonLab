# -*- coding: UTF-8 -*-

from datetime import datetime
from pywinauto import application , Desktop
from time import sleep

app = application.Application(backend="win32") # Win32 API(Default 32bit App)
#app = application.Application(backend="uia") # MS UI Automation

app.start("notepad.exe")
# app.connect_(process = 2341) # ProcessConnect
print app.process

#dlg = Desktop(backend="uia").Calculator
#dlg.type_keys('2*3=')
#dlg.print_control_identifiers()

# 起動したアプリの Top Window の取得
dialog = app.top_window_()
#dialogs = app.window_()

dialog.print_control_identifiers()
#dialogs.print_control_identifiers()

#for dig in dialogs:
#    dig.print_control_identifiers

