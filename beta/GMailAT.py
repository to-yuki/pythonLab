# -*- coding: UTF-8 -*-

# GMail簡易送信モジュール
import gmail

# GMailアカウント情報
sendUsername = #u"from_user@gmail.com"
sendUserPassword = #u"from_user_password"

# メール送信パラメータ
subject = u"件名"
toAddr = #u"to_user@gmail.com"
body = u"本文" 

try:
    # メールサーバに接続して、ログインとメール送信
    print(u"メール送信開始")
    client = gmail.GMail(sendUsername, sendUserPassword)
    message = gmail.Message(subject=subject,to=toAddr,text=body)
    client.send(message)
    client.close()
    print(u"メール送信完了!")
except:
    # メール送信エラー時の対処
    try:
        client.close()
    except:
        pass
    print(u"メール送信エラーです。")