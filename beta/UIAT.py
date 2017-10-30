# coding: utf-8
# pylint: disable=invalid-name

from datetime import datetime
from pywinauto import application
from time import sleep

app = application.Application()
app.start("notepad.exe")

# Notepad クラス (Notepad のウィンドウ) を探して日時を入力
app.Notepad.Edit1.SetText(unicode(datetime.now()))
# メニューを選択
app.Notepad.MenuSelect(u"ファイル->名前を付けて保存")
# 「名前を付けて保存」のウィンドウを探す
dialog = app[u"名前を付けて保存"]
# ファイル名を設定
dialog.Edit1.SetText(u"datetime.txt")
# 保存ボタンをクリック
dialog.Button1.Click()

# すでにファイルが存在すれば上書きの確認が求められる
confirm = app[u"名前を付けて保存の確認"]
if confirm.Exists():  # 確認を求められたかどうか
    print 'Update'
    confirm.Button1.Click() # 上書きする
    confirm.Button1.Click() # もう一度クリックｌｓ

# キーストロークを使って終了させる
app.Notepad.TypeKeys("%FX") # 終了 (Alt+F X)