# -*- coding: utf-8 -*-
# @Time : 2021/11/16 22:36
# @Author : Liangjiajing
# @FileName: myEmail.py
# @Email : 1369462217@qq.com
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = '1369462217@qq.com'
receiver = '1369462217@qq.com'
subject = 'xxxx'
smtpserver = 'smtp.qq.com'
username = '1369462217@qq.com'
password = 'xxxxx'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

# 构造附件
att = MIMEText(open('path', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="xxxx"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()