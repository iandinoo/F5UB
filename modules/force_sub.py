from modules.database import get_force_subs

async def check_force_sub(client, user_id):
    for chat_id in get_force_subs():
        try:
            member = await client.get_chat_member(chat_id, user_id)
            if member.status in ["left", "kicked"]:
                return False
        except:
            return False
    return True
  
