from pymongo import MongoClient
from config import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client["filesharingbot"]

settings = db.settings
admins = db.admins
forcesubs = db.forcesubs
users = db.users
files = db.files


def get_setting(key):
    data = settings.find_one({"_id": key})
    return data["value"] if data else None


def set_setting(key, value):
    settings.update_one(
        {"_id": key},
        {"$set": {"value": value}},
        upsert=True
    )


# ---------- ADMINS ----------
def add_admin(user_id):
    admins.update_one({"_id": user_id}, {"$set": {}}, upsert=True)


def del_admin(user_id):
    admins.delete_one({"_id": user_id})


def get_admins():
    return [x["_id"] for x in admins.find()]


# ---------- FORCE SUB ----------
def add_force_sub(chat_id):
    forcesubs.update_one({"_id": chat_id}, {"$set": {}}, upsert=True)


def del_force_sub(chat_id):
    forcesubs.delete_one({"_id": chat_id})


def get_force_subs():
    return [x["_id"] for x in forcesubs.find()]


# ---------- USERS ----------
def save_user(user_id):
    users.update_one({"_id": user_id}, {"$set": {}}, upsert=True)


def del_user(user_id):
    users.delete_one({"_id": user_id})


def get_all_users():
    return [x["_id"] for x in users.find()]


# ---------- FILES ----------
def save_file(code, message_id):
    files.insert_one({"_id": code, "msg_id": message_id})


def get_file(code):
    data = files.find_one({"_id": code})
    return data["msg_id"] if data else None
                      
