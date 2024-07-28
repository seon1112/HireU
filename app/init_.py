from flask import Flask
from .routes import init_routes
from .models import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    # Initialize routes
    init_routes(app)

    # Initialize database
    init_db(app)

    return app
