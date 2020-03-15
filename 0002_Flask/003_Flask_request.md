### Flask
## request
request在Flask中表示当前请求的renquest对象，request对象中保存了一次HTTP请求的所有信息

## request常用的属性：
- data： 记录请求的数据(form表单除外)，并转化为字符串
- form（MultiDict）： 记录请求中的表单数据
- args(MultiDict)： 记录请求中的查询参数（在url中：QueryString）
- cookies(Dict)： 记录请求中的cookies信息（反爬）
- headers(EnvironHeaders)： 记录请求中的报文头（反爬）
- method(GET/POST)： 记录请求使用的HTTP方法（区分业务逻辑）
- url(string)： 记录请求的url地址
- files： 记录请求上传的文件

```python
from flask import Flask

app = Flask(__name__)

# 接口：API
# 127.0.0.1：5000/index?city=shenzhen&country=china  ?后面的称之为查询字符串QueryString
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        pass
    elif request.method == "POST":
        pass
    else:
        pass
    # request 中包含了前端发送过来的所有请求数据
    # 通过request.form可以直接提取请求体重的表单格式数据，是一个类字典的对象
    # name = request.form["name"]
    # 不要使用上面这种方式写，这种方式容易报错
    name = request.form.get("name")
    # 不存在则返回None
    # 通过get方法只能拿到多个同名参数的第一个（字典不可重复键）
    name_list = request.form.getlist("name")
    # getlist方法可以获得多个同名参数的值
    # name = request.form.get("name"， "alex")
    # 不存在的时候，返回默认值：alex
    age = request.form.get("age")
    print(request.data)
    # args是用来提取url中的参数的（查询字符串QueryString）
    city = request.args.get("city")
    city_list = request.args.getlist("city")
    return "hello, name={}, age={}".format(name, age)

@app.route("/upload", methods=["POST"])
def upload():
    file_obj = request.files.get('pic')
    # file_obj 是一个文件对象
    # ‘pic’是键的名称，并不是文件的名称
    if file_obj == None:
        return "未上传文件"
    # 将文件保存到本地
    # 1. 创建一个文件
    f = open("./demo.jpg", "wb")
    # 2. 向文件写内容
    file_data = file_obj.read()
    f.write(file_data)
    # 3. 关闭文件
    f.close()

    # 或者直接使用上传的文件对象：也就是file_obj: 这个文件对象已经不是普通的文件对象
    # flask 对这个文件对象做了一次封装，所以也可以使用下面的写法
    file_obj.save("/home/www/demo1.png")
    return "文件上传成功"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## with 详解

```python
class Foo(object):
    def __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit called")
        print(exc_type)
        print(exc_val)
        print(exc_tb)

with Foo() as foo:
    print("hello start")
    a = 1/0
    print("hello end")

# with： 上下文管理器
# 上面的代码说明，with远远不止可以控制文件
# with可以控制所有类，只要这个类有__enter__、__exit__这两个方法
# 使用with的时候，
# 第一个会执行__enter__，
# 第二，执行你想执行的内容: 就是with 下面你写的代码。
# 第三，执行__exit__
```
