from pymongo import MongoClient


class EmailMongo(object):
    def __init__(self):
        self.client = MongoClient(host="127.0.0.1", port=27017)
        # 可以简写成client = MongoClient(),默认连接本地的默认端口
        self.db = self.client["mailsendDB"]

    def update_title_content(self, title, content):
        collection = self.db["title_content"]
        collection.insert({"title":title, "content":content})
        print("插入数据完成")

    def insert_rev_info(self, rev_addr):
        collection = self.db["rev_addrs"]
        collection.insert({"rev_addr":rev_addr})

    def insert_sender_info(self, sender_addr, sender_pwd):
        collection = self.db["sender_infos"]
        collection.insert({"sender_addr":sender_addr, 'sender_pwd':sender_pwd})

    def get_title_content(self):
        collection = self.db["title_content"]
        newest = collection.find_one(sort=[('_id', -1)])
        # row = handler.find_one(sort=[('_id', -1)])
        print('---------------------', newest)
        return newest

    def get_all_senders(self):
        collection = self.db["sender_infos"]
        return collection.find()

    def get_all_rev_emalis(self):
        collection = self.db["rev_addrs"]
        return collection.find()

    def delete_sender(self, email):
        collection = self.db["sender_infos"]
        myquery = {
            "sender_addr": email
        }
        collection.delete_one(myquery)

    def clean_database(self):
        collection = self.db["rev_addrs"]
        collection.drop()
        collection = self.db["sender_infos"]
        collection.drop()
