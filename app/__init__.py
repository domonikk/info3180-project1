from flask import Flask
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)
app.config['SECRET_KEY'] = "cheesecake"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zwmbduvsujxiir:08501009c31f3fd62bb6b5e58151d811717080a2ae96051eeddc0fb0ba19a8fa@ec2-54-243-243-136.compute-1.amazonaws.com:5432/dco681jp648vl5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
