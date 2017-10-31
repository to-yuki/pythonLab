# -*- coding: UTF-8 -*-

from datetime import datetime
from pywinauto import application
from time import sleep

app = application.Application(backend="win32") # Win32 API(Default)
app.start("notepad.exe")
dialog = app.top_window_()
dialog.print_control_identifiers()

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
dialog.Button2.Click()
dialog.Button2.Click()

# すでにファイルが存在すれば上書きの確認が求められる
#confirm = app[u"名前を付けて保存の確認"]
#confirm.print_control_identifiers()
#if confirm.Exists():  # 確認を求められたかどうか
#    print 'Update'
#    confirm.Button1.Click() # 上書きする(アクティブでない時選択)
#    confirm.Button1.Click() # もう一度クリック

# キーストロークを使って終了させる
app.Notepad.TypeKeys("%FX") # 終了 (Alt+F X)