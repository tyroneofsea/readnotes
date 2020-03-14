## Flask
- flask本身相当于一个内核。几乎所有的功能都要用到扩展。
- flask框架的核心就是Werkzeug（路由模块）和Jinja2（模板引擎）

## Django
- django-admin：快速创建项目工程目录
- manage.py： 管理项目工程
- orm模型： 数据库抽象层
- admin： 后台管理站点
- 缓存机制
- 文件存储系统
- 用户认证系统
- ...
### 以上这些flask都没有，哈哈哈，没有鱼丸...
## Flask扩展包
- Flask-SQLalchemy:操作数据库
- Flask-migrate: 管理迁移数据库
- Flask-Mail：邮件
- Flask-WTF：表单
- Flask-script： 插入脚本
- Flask-Login： 认证用户状态
- Flask-RESTful： 开发REST API的工具
- Flask-Bootstrap： 集成前端Bootstrap框架
- Flask-Moment： 本地化日期和时间
- ...
### 都有了！

## 最简单的falsk
```python
from flask import Flask


# 创建flask的应用对象
app = Flask(__name__)
# __name__:表示当前模块名字
# 模块名作用：flask以这个模块所在的目录为总目录
# 默认这个目录中的static为静态文件目录
# 默认这个目录中的templates为模板文件目录

'''
__name__的具体名字：
如果作为启动模块（就是你直接运行当前磨矿）：__name__ =__main__:(python定死的)
如果你从别的地方导入一个模块，而导入的模块中也使用__name__,那么导入模块中的__name__=模块的名字（文件名）
结合 if __name__ == '__main__':来理解，这也就是为什么这个==可以作为入口函数的原因
app = Flask(
    __name__,
    static_url_path="/python",  # 修改静态资源url前缀，默认为/static
    static_folder="static",  # 修改静态文件目录，默认就是static
    template_folder="templates"  # 模板文件目录，默认是templates
)
'''

@app.route("/")
def index():
    """定义视图函数"""
    return "Hello Flask"

if __name__ == '__main__':
    # 启动flask程序
    app.run()
    # app.run(host='', port=5555, DEBUG=True)
    # 绑定端口和IP，设定模式为DEBUG模式（代码有更新，直接刷新就好了）
# 在终端输入：python 你为这个文件命名的.py文件
```
