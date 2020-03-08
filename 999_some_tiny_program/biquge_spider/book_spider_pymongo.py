from pymongo import MongoClient
from settings import *
import urllib



class SpiderMongo(object):
    def __init__(self):
        self.client = MongoClient(host="127.0.0.1", port=27017)
        # 可以简写成client = MongoClient(),默认连接本地的默认端口
        # self.collection = client["keywordsDB"][keywords_colletion]
        print(DATABASE_NAME)
        self.db = self.client[DATABASE_NAME]

    def insert_data_dabases(self, collection, dict_list):
        print("---------------------------insert_data_dabases------------------------------------")
        print(collection)
        print(dict_list)
        print("---------------------------insert_data_dabases------------------------------------")
        collection_name = self.db[collection]
        try:
            res = collection_name.insert(dict_list)

            return True
        except:
            return False
# 下面是测试的内容

# def main():
#     mongoinsert = SpiderMongo()
#     data_for_book_details = {
#         "book_id": "book_id",
#         "book_capter_numb": "book_capter_numb",
#         "book_capter_name": "book_capter_name",
#         "book_content": "book_content"
#     }
#     mongoinsert.insert_data_dabases(DATABASE_NAME, data_for_book_details)
#
#
# if __name__ == '__main__':
#     main()
