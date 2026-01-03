import os

def get_setting(key: str, default=None):
    return os.getenv(key.upper(), default)
  
