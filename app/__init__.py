import imp
from flask import Flask
from config import Config

#import Blueprints
from .auth.routes import auth


app = Flask(__name__)            

#register blueprint
app.register_blueprint(auth)


app.config.from_object(Config)

from . import routes

