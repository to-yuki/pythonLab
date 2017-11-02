# -*- coding: UTF-8 -*-

import gmail
import os

sendUsername = u'to-yuki@jtp.co.jp'
sendUserPassword = u'xxxx'
subject = u"PythonテストMail"
toAddr = u'to-yuki@jtp.co.jp'
body = u"Pythonからのテストメッセージです。" 

client = gmail.GMail(sendUsername, sendUserPassword)
message = gmail.Message(subject=subject,to=toAddr,text=body)
client.send(message)
client.close()