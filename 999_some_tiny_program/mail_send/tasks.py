#tasks.py
from celery import Celery
from mailmongo import EmailMongo
from mail_send import send_mail
app = Celery('tasks',  backend='redis://localhost:6379/0', broker='redis://localhost:6379/0') #配置好celery的backend和broker


@app.task  #普通函数装饰为 celery task
def long_task(keyname):
    print("I am Task")
    mailmongo = EmailMongo()
    newest = mailmongo.get_title_content()
    title = newest['title']
    mail_content = newest['content']
    all_rev_emalis = mailmongo.get_all_rev_emalis()
    all_senders = mailmongo.get_all_senders()
    for rev_email in all_rev_emalis:
        maillist = rev_email["rev_addr"]
        for sender in all_senders:
            email_user = sender["sender_addr"]
            email_pwd = sender["sender_pwd"]
            result = send_mail(email_user, email_pwd, maillist, title, mail_content)
            if result == True:
                print("{}---->{}:成功".format(email_user, rev_email))
                break  # 结束当前循环，因为返回为True，说明发送成功了，所以结束当前循环
            else:
                mailmongo.delete_sender(email_user) # 删除这个发送人，下一次读取不会读到了
                continue # 跳出本次循环，因为返回为False，说明发送失败，找下一个发件人来发送。

    mailmongo.clean_database()
    print("I am Task end")
    return result
