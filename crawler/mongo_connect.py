from pymongo import MongoClient

USER = "root"
PASS = "example"
DBNAME = "test_database"
COLLECTION = "pdf"

class DBConnect:
    def __init__(self):
        try:
            self.client = MongoClient(username = USER, password = PASS)
            self.db = self.client[DBNAME][COLLECTION]
        except Exception as e:
            print(f"Não foi possível conexão com banco de dados: {e}")

    def count(self, filter):
        return self.db.count_documents(filter)

    def insert_one(self, data):
        return self.db.insert_one(data)

    def insert_many(self, data):
        return self.db.insert_many(data)

    def find(self, filter):
        return self.db.find(filter)

    def clear_database(self):
        return self.db.delete_many()
