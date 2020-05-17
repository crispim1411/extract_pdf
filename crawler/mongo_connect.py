from pymongo import MongoClient

USER = "root"
PASS = "example"
DBNAME = "test_database"
COLLECTION = "pdf"

class DBConnect:
    def __init__(self):
        self.client = MongoClient(username = USER, password = PASS)
        self.db = self.client[DBNAME][COLLECTION]

    def count(self, filter):
        return self.db.count_documents(filter)

    def insert_one(self, data):
        self.db.insert_one(data)

    def insert_many(self, data):
        self.db.insert_many(data)

    def find(self, filter):
        return self.db.find(filter)

    def clear_database(self):
        self.db.delete_many()
