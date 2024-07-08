from flask import Flask
from app.extensions import db

#import blueprints
from app.views.main import main
from app.views.auth import auth

def create_app():
    #create app instance
    app = Flask(__name__)

    #configure app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contab.db'
    app.config['SECRET_KEY'] = 'development key'

    #initialize database
    with app.app_context():
        db.init_app(app)
        db.create_all()

    #register blueprints
    app.register_blueprint(main)
    app.register_blueprint(auth)

    #return app instance
    return app