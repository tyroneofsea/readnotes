from pymongo import MongoClient


class KeywordsMongo(object):
    def __init__(self):
        self.client = MongoClient(host="127.0.0.1", port=27017)
        # 可以简写成client = MongoClient(),默认连接本地的默认端口
        # self.collection = client["keywordsDB"][keywords_colletion]
    def test_insert(self, keywords_colletion, context):
        collection_name = self.client["keywordsDB"][keywords_colletion]
        res = collection_name.insert(context)
        print(res)

    def get_info_by_collection_name(self, keywords_colletion):
        db = self.client["keywordsDB"][keywords_colletion]
        results = db.find()
        # for result in results:
        #     print(result)
        return results

    def get_collections_names(self):
        db = self.client["keywordsDB"]
        coll_names = db.list_collection_names(session=None)
        # print(coll_names)
        # print(type(coll_names))
        return coll_names




if __name__ == '__main__':
    testmongo = KeywordsMongo()
    testmongo.get_collections_names()
    testmongo.get_info_by_collection_name("久章草在线视频免费")
