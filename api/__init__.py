import cloudinary
from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import os

app = Flask(__name__)
CORS(app)
config = dotenv_values()

# development
# app.config["SQLALCHEMY_DATABASE_URI"] = config["DATABASE_URL"]
# app.config["SECRET_KEY"] = config["SECRET_KEY"]

# cloudinary.config(
#    cloud_name=config["CLOUDINARY_CLOUD_NAME"],
#    api_key=config["CLOUDINARY_API_KEY"],
#    api_secret=config["CLOUDINARY_API_SECRET"]
# )

# Prod
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET")
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return 'go to /graphql route to send request'
