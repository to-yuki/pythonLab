# -*- coding: UTF-8 -*-
import openpyxl

# 新規のワークブックの作成
book = openpyxl.Workbook()
# 新規作成された最初のシートを取得
sheet = book.active
# シート名を変更(Sheet1 -> シート1)
sheet.title = u"シート1"
# A1 セルに値を設定
sheet["A1"] = u"ハロー"

# A2 のセル以下 A100 まで繰返しデータの設定
for i in range(2,101):
    sheet.cell(row=i,column=1).value = u"Python ワールド"

# ワークブックの保存
book.save("newBook.xlsx")
