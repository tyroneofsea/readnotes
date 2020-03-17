## session

- Flask默认把session的具体的值，设置成了cookie中，只是经过了SECRET_KEY加密
- 当然项目中可以保存到数据库

```python
from flask import Flask, session

app = Flask(__name__)



# flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "SADFdgfhjhgfdssdfghjkhgfd"

@app.route("/login")
def login():
    # 设置session数据
    session["name"] = "alex"
    session["age"] = 18
    return "login success"

@app.route("/index")
def index():
    # 获取session的数据
    name = session.get("name")
    return "hello {}".format(name)

if __name__ == '__main__':
    app.run(host="127.0.0.1", host=5000, debug=True)


```
