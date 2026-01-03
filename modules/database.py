from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["filesharingbot"]

def add_user(user_id):
    db.users.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def get_users():
    return list(db.users.find())

def add_admin(user_id):
    db.admins.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)

def remove_admin(user_id):
    db.admins.delete_one({"_id": user_id})

def get_admins():
    return list(db.admins.find())

def add_file(chat_id, message_id):
    db.files.insert_one({"chat_id": chat_id, "message_id": message_id})

def get_file(file_id):
    return db.files.find_one({"_id": file_id})

def set_setting(key, value):
    db.settings.update_one({"_id": key}, {"$set": {"value": value}}, upsert=True)

def get_setting(key):
    doc = db.settings.find_one({"_id": key})
    return doc["value"] if doc else None

def add_forcesub(chat_id):
    db.forcesub.update_one({"_id": chat_id}, {"$set": {"_id": chat_id}}, upsert=True)

def remove_forcesub(chat_id):
    db.forcesub.delete_one({"_id": chat_id})

def get_forcesubs():
    return list(db.forcesub.find())
    
