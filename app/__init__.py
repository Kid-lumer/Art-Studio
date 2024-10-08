from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    mongo.init_app(app)

    with app.app_context():
        from .routes import user_routes
        from .routes import items_routes
        from .routes import cart_routes

        app.register_blueprint(user_routes.app)
        app.register_blueprint(items_routes.app)
        app.register_blueprint(cart_routes.app)

        
    return app