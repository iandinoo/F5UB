from modules.handlers import register_handlers
from modules.admin import register_admin

def register_routes(app):
    register_handlers(app)
    register_admin(app)
    
