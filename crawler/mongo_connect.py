from pymongo import MongoClient

USER = "root"
PASS = "example"
DBNAME = "test_database"
COLLECTION = "pdf"

class DBConnect:
    def __init__(self):
        self.client = MongoClient(username = USER, password = PASS)
        self.db = self.client[DBNAME][COLLECTION]

    def insert_one(self, data):
        self.db.insert_one(data)

    def find_all(self):
        return self.db.find()

    def clear_database(self):
        self.db.delete_many()
