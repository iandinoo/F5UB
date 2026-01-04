import secrets

def gen_token():
    return secrets.token_urlsafe(12)
    
