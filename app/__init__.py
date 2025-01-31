from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .database import db
from .routes.transactions import transaction_routes
from .routes.auth import auth_routes
from .routes.predict import predict_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Register blueprints
    app.register_blueprint(transaction_routes, url_prefix="/transactions")
    app.register_blueprint(auth_routes, url_prefix="/auth")
    app.register_blueprint(predict_bp, url_prefix="/model") 
    
    @app.route('/')
    def ping():
        return "Server is up and running!", 200

    return app
