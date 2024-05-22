"""..."""
import os
from flask import Flask
from dotenv import load_dotenv
from api.models.__init__ import db  # Import the SQLAlchemy object from your models package

def create_app():
    """Create Flask Application"""
    app = Flask(__name__)

    # Configure app
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://default:q5LJsUYT0DCv@ep-delicate-cake-a41wr4kl-pooler.us-east-1.aws.neon.tech/verceldb'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Load environment variables from .env.local file
    load_dotenv('.env.local')

    # Configure app using environment variables
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database with the Flask app instance
    db.init_app(app)

    from api.routes import init_routes  # Import the function to initialize your routes
    # Initialize routes
    init_routes(app)

    @app.route('/')
    def index():
        """..."""
        return "Hello, World!"

    return app
