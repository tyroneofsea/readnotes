### pymongo
## 安装
```python
# 在虚拟环境中
pip install pymongo
```
## 来个最简单的例子
```python
from pymongo import MongoClient


class TestMongo(object):
    def __init__(self):
        client = MongoClient(host="127.0.0.1", port=27017)
        # 可以简写成client = MongoClient(),默认连接本地的默认端口
        self.collection = client["testDB"]["testColletion"]
    def test_insert(self):
        res = self.collection.insert({name:"skt", age: 33})
        print(res)

    def test_insert_many(self):
        items_list = [{name:"test{}".format(i)} for i in range(1000000)]
        res = self.collection.insert_many(items_list)
        for i in res.inserted_ids:
            print(i)

if __name__ == '__main__':
    testmongo = TestMongo()
    testmongo.test_insert()
    testmongo.test_insert_many()

```
