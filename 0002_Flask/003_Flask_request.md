### Flask
## request
request在Flask中表示当前请求的renquest对象，request对象中保存了一次HTTP请求的所有信息

## request常用的属性：
- data： 记录请求的数据，并转化为字符串
- form（MultiDict）： 记录请求中的表单数据
- args(MultiDict)： 记录请求中的查询参数
- cookies(Dict)： 记录请求中的cookies信息
- headers(EnvironHeaders)： 记录请求中的报文头
- method(GET/POST)： 记录请求使用的HTTP方法
- url(string)： 记录请求的url地址
- files： 记录请求上传的文件

```python
from flask import Flask

app = Flask(__name__)

@app.route("/index", methods=["GET", "POST"])
def index():
    # request 中包含了前端发送过来的所有请求数据
    # 通过request.form可以直接提取请求体重的表单格式数据，s是一个类字典的对象
    # name = request.form["name"]
    # 不要使用上面这种方式写，这种方式容易报错
    name = request.form.get("name")
    # 不存在则返回None
    # name = request.form.get("name"， "alex")
    # 不存在的时候，返回默认值：alex
    age = request.form.get("age")
    return "hello, name={}, age={}".format(name, age)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
