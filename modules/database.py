from pymongo import MongoClient
from config import MONGODB_URL

client = MongoClient(MONGODB_URL)
db = client["f5ub"]

files_col = db["files"]
settings_col = db["settings"]

def save_file(token, file_id):
    files_col.insert_one({
        "token": token,
        "file_id": file_id
    })

def get_file(token):
    return files_col.find_one({"token": token})

def get_setting(key):
    data = settings_col.find_one({"key": key})
    return data["value"] if data else None

def set_setting(key, value):
    settings_col.update_one(
        {"key": key},
        {"$set": {"value": value}},
        upsert=True
    )
    
