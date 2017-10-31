# -*- coding: UTF-8 -*-

from datetime import datetime
from pywinauto import application
from time import sleep

#sleep time
sleepSec=1

# Win32 API(Default)
app = application.Application(backend="win32") 
app.start("notepad.exe")
#dialog = app.top_window_()
#dialog.print_control_identifiers()

# Notepad クラス (Notepad のウィンドウ) を探して日時を入力
app.Notepad.Edit.SetText(unicode(datetime.now()))

# メニューを選択
app.Notepad.MenuSelect(u"ファイル->名前を付けて保存")

# 「名前を付けて保存」のウィンドウを取得
dialog = app[u"名前を付けて保存"]
#dialog.print_control_identifiers()

# ファイル名を設定
dialog.Edit.SetText(u"datetime.txt")

# 保存ボタンをクリック
saveButtion = dialog[u'保存(&S)'] # 保存ボタンの取得
saveButtion.Click() # ボタンをクリック
saveButtion.Click() # ボタンをクリック(タイミングにより反応しな場合はもう一度) 

# すでにファイルが存在すれば上書きの確認が求められる
confirm = app[u"名前を付けて保存の確認"]
#confirm.print_control_identifiers()
if confirm.Exists():  # 確認を求められたかどうか
    print 'Update'
    confirmButtion = confirm[u'はい(&Y)'] # はいボタンの取得
    confirmButtion.Click() # ボタンをクリック
    # confirmButtion.Click() # ボタンをクリック(タイミングにより反応しな場合はもう一度) 

# キーストロークを使って終了させる
sleep(sleepSec) # Window の更新が終わるのを待って終了
app.Notepad.MenuSelect(u"ファイル->メモ帳の終了")