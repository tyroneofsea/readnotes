from pymongo import MongoClient


class TestMongo(object):
    def __init__(self, keywords_colletion):
        client = MongoClient(host="127.0.0.1", port=27017)
        # 可以简写成client = MongoClient(),默认连接本地的默认端口
        self.collection = client["keywordsDB"][keywords_colletion]
    def test_insert(self, context):
        res = self.collection.insert(context)


if __name__ == '__main__':
    testmongo = TestMongo()
    testmongo.test_insert()
    testmongo.test_insert_many()
