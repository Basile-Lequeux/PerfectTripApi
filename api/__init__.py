from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from credentials import postgresql_dev
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config[
    "SQLALCHEMY_DATABASE_URI"] = postgresql_dev
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def hello():
    return 'go to /graphql route to send request'
