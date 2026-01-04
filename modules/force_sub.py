from pyrogram.enums import ChatMemberStatus
from config import FORCE_SUB_CHANNELS

async def check_force_sub(client, user_id):
    not_joined = []

    for chat_id in FORCE_SUB_CHANNELS:
        try:
            member = await client.get_chat_member(chat_id, user_id)
            if member.status not in (
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER
            ):
                not_joined.append(chat_id)
        except:
            not_joined.append(chat_id)

    return not_joined
    
