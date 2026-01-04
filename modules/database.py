from pymongo import MongoClient
from config import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client["filesharingbot"]

users = db.users
files = db.files
settings = db.settings
admins = db.admins
forcesub = db.forcesub


def add_user(user_id: int):
    users.update_one({"_id": user_id}, {"$set": {"_id": user_id}}, upsert=True)


def get_users():
    return [u["_id"] for u in users.find()]


def set_setting(key, value):
    settings.update_one({"_id": key}, {"$set": {"value": value}}, upsert=True)


def get_setting(key, default=None):
    d = settings.find_one({"_id": key})
    return d["value"] if d else default
    
