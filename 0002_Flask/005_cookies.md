## cookies

```python
from flask import Flask, make_response

app = flask(__name__)


@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")
    # 设置cookies，默认有效期是临时cookie，浏览器关闭就消失
    # 第一个参数是键名，第二个参数是值
    resp.set_cookie("name", "alex")
    resp.set_cookie("age", 18)
    # max_age 设置有效时间， 单位：秒
    resp.set_cookie("city", "beijing", max_age=3600)
    # 上面的方法，其实和下面的方法达到的效果是一样的
    resp.headers["Set-Cookie"] = "name=alex;age=24;Max-Age:3600"
    return resp

@app.route("/get_cookie"):
def get_cookie():
    c = requset.cookies.get("name")
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("name")
    # 并不会真的删除这个cookie而是把这个cookie的有效时间设置成0
    return resp

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
```


## 安装postman  模拟发送请求
