from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client["filesharingbot"]

users = db.users
admins = db.admins
files = db.files
settings = db.settings
forcesub = db.forcesub

def add_user(uid):
    users.update_one({"_id": uid}, {"$set": {}}, upsert=True)

def get_users():
    return list(users.find())

def add_admin(uid):
    admins.update_one({"_id": uid}, {"$set": {}}, upsert=True)

def get_admins():
    return list(admins.find())

def remove_admin(uid):
    admins.delete_one({"_id": uid})
    
