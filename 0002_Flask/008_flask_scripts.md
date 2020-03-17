## 像 Django 一样来启动Flask

pip3 install flask
```python
from flask import Flask
from flask_script import Manager

app = Flask(__name__)

# 创建Manager管理类的对象
manager = Manager(app)

@app.route("/index")
def index():
    return "index page"

if __name__ == '__main__':
    # app.run(host="127.0.0.1", port=5000, debug=True)
    # 通过管理对象来启动flask
    manager.run()

'''
python 该文件名.py --help
python 该文件名.py runserver --help
python 该文件名.py runserver -h 127.0.0.1 -p 8888
'''
```
