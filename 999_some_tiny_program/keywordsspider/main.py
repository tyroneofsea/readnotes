from flask import Flask, request, render_template
import keywordsspider
from mongomanager import KeywordsMongo
from tasks import long_task


__all__ = ['app']
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('alex.html')

@app.route('/q', methods=['GET','POST'])
def searche():
    print(request.args.get('name'))
    keyname = request.args.get('name')
    if keyname == '':
        return '<h2>空值查询什么呢...</h2>'

    try:
        certen_nub = int(request.args.get('c'))
    except:
        certen_nub = None
    print("certen_nub=",certen_nub)
    if certen_nub is not None:
        task = long_task.delay(keyname)
        return '<h2>后台已经再执行程序了，请20分钟以后查看...</h2>'

    km = KeywordsMongo()
    qname_list = km.get_collections_names()

    if len(qname_list) == 0:
        # kspider = keywordsspider.KeywordsSpider(keyname)
        # return_context = kspider.get_urls_from_baidu()
        task = long_task.delay(keyname)
        return '<h2>后台已经再执行程序了，请20分钟以后查看...</h2>'

    if (keyname in qname_list):
        results = km.get_info_by_collection_name(keyname)
        return_context = []
        for result in results:
            return_context.append(result)
        return render_template('exist_data.html', context=return_context)
    else:
        task = long_task.delay(keyname)
        return '<h2>后台已经再执行程序了，请20分钟以后查看...</h2>'

    # if len(qname_list) == 0 or certen_nub==1 :
    #     kspider = keywordsspider.KeywordsSpider(keyname)
    #     return_context = kspider.get_urls_from_baidu()
    #     if len(return_context) == 0:
    #         return '<h2>baidu_url 读取错误, 可能该词被百度屏蔽，请再试一次！ </h2><br>'
    #     print("return_context=",return_context)
    #     print(type(return_context))
    #     return render_template('alex.html', context=return_context)





if __name__ == '__main__':
    app.run()
