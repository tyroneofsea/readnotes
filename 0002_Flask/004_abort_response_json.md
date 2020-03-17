## abort(): 终止当前视图函数，并返回一个结果给前端
- 传递参数值(必须是标准的http状态码)： abort(400), abort(500), abort(302), abort(404)
- 传递响应体信息(必须封装成Response对象，直接传字符串不行)： abort(Response("请求错误"))

## response
- 使用元组：
    -- return "index page", 400,

```python
from flask import Flask, requset, Response, abort, make_response, jsonify
import json


app = Flask(__name__)


@app.route("login", methods=["GET"])
def login():
    name = ""
    pwd = ""
    if name != "zhangsan" or pwd != "admin":
        # 1. 传递参数值
        abort(403)
        # 2. 传递响应体信息
        # resp = Response("login error")
        # abort(resp)
        # 想一下为什么不用下面这种
        # 因为这和retrun 一个字符串没有区别，还不如返回一个字符串

@app.errorhandler(404)
def handler_404_error(err):  # 必须接受一个参数，名称随意
    """自定义的处理错误的方法"""
    # 这个函数的返回值会是前端用户看到的结果
    return "出现了404错误， 错误信息：{}".format(err)

@app.route("/index")
def index():
    # 1. 使用元组， 返回自定的响应信息
    #格式： 响应体-------状态码-响应头
    return "index page", 400, [("age": 18), ("City": "hangzhou")]
    return "index page", 400, {"age": 18, "City": "hangzhou"}
    return "index page", 666, {"age": 18, "City": "hangzhou"}
    return "index page", "666 ACB status", {"age": 18, "City": "hangzhou"}
    return "index page", "666 ACB status"
    # 2。 使用make_response 来构造响应信息
    resp = make_response("index page")
    resp.status = "999 fanpa"  # 设置状态码
    resp.headersp["city"] = "beijing"  # 设置响应头
    return resp

@app.route("/json")
def json():
    # json就是字符串
    # 记得在上方导入json： import json
    data = {
        "name": "python",
        "age": 18
    }
    # json.dumps(字典)： 将字典转化为字符串
    # json.loads(字符串)： 将字符串转化为字典
    json_str = json.dumps(data)
    return json_str  # 前端并不知道这个是json，查看返回类型，是text
    return json_str, 200, {"Content-Type": "application/json"}  # 完美返回json，但是繁琐
    # 记得在上方导入： form flask import jsonify
    # jsonify帮助转化为json数据，并设置相应头（为了让前端知道这个是响应头）
    return jsonify(data)
    return jsonify("name": "ABC", "age": 45)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
