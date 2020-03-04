from flask import Flask, request, render_template
import keywordsspider

__all__ = ['app']
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>欢迎来到Alex查询标题、关键词、描述</h2><br>'

@app.route('/q', methods=['GET','POST'])
def searche():
    print(request.args.get('name'))
    kspider = keywordsspider.KeywordsSpider(request.args.get('name'))
    return_context = kspider.get_urls_from_baidu()
    if len(return_context) == 0:
        return '<h2>baidu_url 读取错误, 可能该词被百度屏蔽，请再试一次！ </h2><br>'
    print("return_context=",return_context)
    print(type(return_context))
    # context = {}
    # for i in range(0, len(return_context)):
    #     context.append(return_context[i])
    # # return '<h2>' + request.args.get('name') + '</h2><br>'
    # print(type(context))
    # print(context)
    return render_template('alex.html', context=return_context)


if __name__ == '__main__':
    app.run()
