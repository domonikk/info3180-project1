from flask import Flask
from flask_sqlalchemy import SQLAlchemy 



app = Flask(__name__)
app.config['SECRET_KEY'] = "cheesecake"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:project1@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = './app/static/images'

db = SQLAlchemy(app)


app.config.from_object(__name__)
from app import views
