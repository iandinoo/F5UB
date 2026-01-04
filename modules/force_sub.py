from pyrogram.errors import UserNotParticipant
from modules.database import forcesub

async def check_force_sub(client, user_id: int):
    chans = list(forcesub.find())
    for c in chans:
        try:
            await client.get_chat_member(c["_id"], user_id)
        except UserNotParticipant:
            return False
    return True
    
