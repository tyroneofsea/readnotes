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
        # print("---------------------------insert_data_dabases------------------------------------")
        # print(collection)
        # print(dict_list)
        # print("---------------------------insert_data_dabases------------------------------------")
        collection_name = self.db[collection]
        try:
            res = collection_name.insert(dict_list)
            return True
        except:
            return False

    def is_book_id_in_mongodb(self, book_id):
        collection_name = self.db['book_infos']
        return collection_name.find_one({"book_id": book_id})


    def get_newest_capter_numb_from_mongodb(self, book_id):
        collection_name = self.db['book_details']
        results =  collection_name.find({"book_id": book_id}).sort('_id', -1).limit(1)
        return_list = []
        for result in results:
            return_list.append(result)
        print(return_list)

    def update_book_infos_by_book_id(self, book_id, data_list):
        collection_name = self.db['book_infos']
        condition = {'book_id': book_id}
        book_infos = collection_name.find_one(condition)
        book_infos[INFOS_STATUS] = data_list[INFOS_STATUS]
        book_infos[INFOS_LAST_UPDATE_TIME] = data_list[INFOS_LAST_UPDATE_TIME]
        book_infos[INFOS_LAST_UPDATE_DESC] = data_list[INFOS_LAST_UPDATE_DESC]
        book_infos[INFOS_LAST_UPDATE_URL] = data_list[INFOS_LAST_UPDATE_URL]
        result = collection_name.update_one(condition, {'$set': book_infos})
        print(result)





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
