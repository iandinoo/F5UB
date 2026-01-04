from modules.database import get_users

async def do_broadcast(client, from_user, message):
    success = 0
    failed = 0

    for uid in get_users():
        if uid == from_user:
            continue
        try:
            await message.copy(uid)
            success += 1
        except:
            failed += 1

    return success, failed
  
