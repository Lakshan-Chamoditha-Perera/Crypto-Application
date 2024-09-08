from pymongo import MongoClient
from config.config import Config

client = MongoClient(Config.MONGO_URI)
db = client['crypto']

class User:
    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password

    def save(self):
        db.users.insert_one(self.__dict__)

    @staticmethod
    def find_by_id(user_id):
        return db.users.find_one({"_id": user_id})

    @staticmethod
    def find_all():
        return list(db.users.find())

class Transaction:
    def __init__(self, value, sender_id, receiver_id):
        self.value = value
        self.sender_id = sender_id
        self.receiver_id = receiver_id

    def save(self):
        db.transactions.insert_one(self.__dict__)

    @staticmethod
    def find_by_id(transaction_id):
        return db.transactions.find_one({"_id": transaction_id})

    @staticmethod
    def find_all():
        return list(db.transactions.find())
