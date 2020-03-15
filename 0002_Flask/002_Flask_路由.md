## Flask 路由规则

```python
from flask import Flask
from werkzeug.routing import BaseConverter


app = Flask(__name__)

@app.route("/")
def index():
    return 'hello Flask'

# 通过methods来限定访问方式
@app.route("/post_get", methods=["GET", "POST"])
def post_get():
    return "POST_GET PAGE"

# 同一个函数，两个路径
@app.route("/hi1")
@app.route("/hi2")
def hi():
    return 'hi page hi1, hi2'

# 使用url_for的函数，通过视图函数的名字找到视图对应的url路径
# 记得在上方导入from flask import redirect, url_for
@app.route("/login")
def login():
    url = url_for("index")
    return redirect(url)

# <int:book_id>
# int:转化器类型，可以省略，如果省略，那么他默认为字符串
# 转化器，有三种：int、string、path
# book_id:参数名称，记得传入函数
@app.route("/book/<int:book_id>/<int:book_capter>")
def book_details(book_id， book_capter):
    return "{}book {} page".format(book_id, book_capter)

# 1. 定义自己的转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super().__init__(url_map)
        # python2写法：
        # super(BaseConverter, self).__init__(url_map)
        # 将自己的正则表达的参数，保存到对象的属性中，falsk会去使用这个属性来进行路由的正则匹配
        self.regex = regex

# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
# http://127.0.0.0:5000/send/18888888888
@app.route("/send/<re(r'1[34578]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to {}".format(mobile)


if __name__ == '__main__':
    # 通过url_map可以查看整个flask中的所有路由信息
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000, debug=True)
```
