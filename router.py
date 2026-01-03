from modules.handlers import register_handlers

class Router:
    def register(self, app):
        register_handlers(app)

router = Router()
