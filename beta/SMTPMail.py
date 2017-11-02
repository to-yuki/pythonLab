# -*- coding: UTF-8 -*-

import smtplib
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate

# メール送信パラメータ
date = formatdate()
encoding = "utf-8"
subject = u"件名"
body = u"本文".encode('utf-8')
from_addr = u"from_user@gmail.com"
to_addrs = u"to_user@gmail.com"
username = u"from_user@gmail.com"
passwd = u"from_user_password"
smtphost = "smtp.gmail.com"
smtpport = 587 

# メールメッセージの組み立て
msg = MIMEText(body, "plain", encoding)
msg["Subject"] = Header(subject, encoding)
msg["From"] = from_addr
msg["To"] = to_addr
msg["Date"] = date

# メールサーバに接続して、ログインとメール送信
smtpcon = None
try:
    smtpcon = smtplib.SMTP(smtphost, smtpport)
    smtpcon.ehlo()
    smtpcon.starttls()
    smtpcon.ehlo()
    smtpcon.login(username,passwd)
    smtpcon.sendmail(from_addr,to_addrs,msg.as_string())
    smtpcon.close()
except:
    try:
        smtpcon.close()
    except:
        pass
    print(u"メール送信エラーです。")