#!/usr/bin python3
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

class EmailSendClass(object):
    def send_mail(username, passwd, recv, title, content, mail_host='smtp.naver.com', port=465):
        '''
        发送邮件函数，默认使用163smtp
        :param mail_host: 邮箱服务器，16邮箱host: smtp.163.com
        :param port: 端口号,163邮箱的默认端口是 25  SSL端口为465/994
        :param username: 邮箱账号 xx@163.com
        :param passwd: 邮箱密码(不是邮箱的登录密码，是邮箱的授权码)
        :param recv: 邮箱接收人地址，多个账号以逗号隔开
        :param title: 邮件标题
        :param content: 邮件内容
        :return:
        '''
        msg = MIMEText(content)  # 邮件内容
        msg['Subject'] = title  # 邮件主题
        msg['From'] = username  # 发送者账号
        msg['To'] = recv  # 接收者账号列表
        try:
            smtp = smtplib.SMTP_SSL(mail_host, port=port)  # 连接邮箱，传入邮箱地址，和端口号，smtp的端口号是25 SSL端口为465/994
            smtp.login(username, passwd)  # 登录发送者的邮箱账号，密码
            # 参数分别是 发送者，接收者，第三个是把上面的发送邮件的 内容变成字符串
            smtp.sendmail(username, recv, msg.as_string())
            smtp.quit()  # 发送完毕后退出smtp
            print('email send success.')
            return True
        except:
            print("邮件发送失败")
            return False

# email_user = 'tyroneofsea@naver.com'  # 发送者账号
# email_pwd = '0451392aa##'  # 发送者密码,授权码
# maillist = 'tyroneofsea@gmail.com'
# title = 'test1'
# mail_content = 'test1'
# send_mail(email_user, email_pwd, maillist, title, mail_content)
