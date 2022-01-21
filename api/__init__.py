from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os
app = Flask(__name__)
CORS(app)
config = dotenv_values()

#development
#app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE_URL"]
#app.config["SECRET_KEY"] = config["SECRET_KEY"]

#Prod
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return 'go to /graphql route to send request'
