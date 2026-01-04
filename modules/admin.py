from config import OWNER_ID
from modules.database import admins

def is_admin(user_id: int):
    if user_id == OWNER_ID:
        return True
    return admins.find_one({"_id": user_id}) is not None
    
