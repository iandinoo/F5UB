def generate_link(file_id):
    return f"https://t.me/YourBot?start={file_id}"

def format_users(users):
    return "\n".join([str(u["_id"]) for u in users])

def format_admins(admins):
    return "\n".join([str(a["_id"]) for a in admins])
    
