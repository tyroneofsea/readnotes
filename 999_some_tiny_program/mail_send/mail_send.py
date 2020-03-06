from email.header import Header #处理邮件主题
from email.mime.text import MIMEText # 处理邮件内容
from email.utils import parseaddr, formataddr #用于构造特定格式的收发邮件地址
import smtplib #用于发送邮件
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr = '******@163.com'
password = '授权码'
to_addr = 'QQ号@qq.com'
smtp_server = 'smtp.163.com'
msg = MIMEText('Python 爬虫爬取', 'plain','utf-8')
msg['From'] = _format_addr('发送<%s>'%from_addr)
msg['To'] = _format_addr('接收<%s>'%to_addr)
msg['Subject'] = Header('这是邮件主题：一号爬虫运行','utf-8').encode()
server = smtplib.SMTP(smtp_server,25)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
