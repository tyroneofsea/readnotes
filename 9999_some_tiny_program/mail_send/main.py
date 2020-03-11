from flask import Flask, render_template, request, redirect, url_for
from mailmongo import EmailMongo
import re
from tasks import long_task


__all__ = ['app']
app = Flask(__name__)


def check_infos():
    emailmongo = EmailMongo()
    title_content = emailmongo.get_title_content()
    # print(title_content['title'])
    # print(title_content['content'])


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/titlecontext', methods=['GET', 'POST'])
def mailtitlecontext():
    if request.method == 'POST':
        title = request.form['mail_title']
        content = request.form['mail_content']
        print("标题：", title)
        print("内容：", content)
        emailmongo = EmailMongo()
        emailmongo.update_title_content(title, content)
        context = {
            'res': '第一步：邮件内容修改成功'
        }
        return render_template('index.html', context=context)
    return render_template('title_context.html')


@app.route('/rev', methods=['GET', 'POST'])
def save_rev_send():
    if request.method == 'POST':
        rev_text = request.form['rev_list']
        print(rev_text)
        rev_list = re.split(';', rev_text)
        print(rev_list)
        if len(rev_list) == 0:
            context = {
                'res': '第三步：收件人信息上传有误！收件人信息有误！收件人信息有误！'
            }
            return render_template('index.html', context=context)
        emailmongo = EmailMongo()
        for i in range(0, len(rev_list)):
            emailmongo.insert_rev_info(rev_list[i])
        check_infos()
        # task = long_task.delay()
        context = {
            'res': '第三步：收件人上传成功,邮件已经再后台发送了!邮件已经再后台发送了!邮件已经再后台发送了!'
        }
        return render_template('index.html', context=context)
    return render_template('rev_info.html')


@app.route('/sender', methods=['GET', 'POST'])
def save_sender_send():
    if request.method == 'POST':
        sender_text = request.form['sender_text']
        print(sender_text)
        sender_list = re.split(';', sender_text)
        print(sender_list)
        if len(sender_list) == 0:
            context = {
                'res': '第二步：发件人信息上传有误！发件人信息有误！发件人信息有误！'
            }
            return render_template('index.html', context=context)
        emailmongo = EmailMongo()
        for i in range(0, len(sender_list)):
            sender_kv = re.split('----', sender_list[i])
            if len(sender_kv) == 2:
                emailmongo.insert_sender_info(sender_kv[0], sender_kv[1])
            else:
                context = {
                    'res': '第二步：发件人信息上传有误！发件人信息有误！发件人信息有误！(格式错了)'
                }
                return render_template('index.html', context=context)
        print(sender_list)
        context = {
            'res': '第三步：发件人上传成功'
        }
        return render_template('index.html', context=context)
    return render_template('sender_info.html')



if __name__ == '__main__':
    app.run(debug=True)
