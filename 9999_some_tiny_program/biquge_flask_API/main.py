from flask import Flask, jsonify
import json
from flask_pymongo import PyMongo
# pip install Flask-PyMongo 记得安装

app = flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/books")


@app.errorhandler(404)
def handler_404_error(err):  # 必须接受一个参数，名称随意
    """自定义的处理错误的方法"""
    # 这个函数的返回值会是前端用户看到的结果
    return "出现了404错误， 错误信息：{}".format(err)

# 首页接口
@app.route("/index")
def index():
    pass

# 分类页接口
@app.route("/book/<str:book_class>")
def book_class(book_class):
    pass

# 图书首页接口
@app.route("/book/<int:book_id>")
def book_index(book_id):
    if book_id:
        book_index_info = mongo.db.book_infos.find({'book_id': book_id})
        print(type(book_index_info))
        print(book_index_info)
        if book_index_info:
            return jsonify(book_index_info)
        else:
            return 404

# 图书每一章接口
@app.route("/book/<int:book_id>/<int:book_detail_id>")
def book_detail(book_id, book_detail_id):
    if book_id and book_detail_id:
        book_detail_infos = mongo.db.book_details.find({'book_id': book_id, 'book_detail_id': book_detail_id})
        if book_detail_infos:
            return jsonify(book_detail_infos)
        else:
            return 404




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
