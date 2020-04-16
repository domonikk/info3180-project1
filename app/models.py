from . import db
import datetime


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    firstname = db.Column(db.String(40))
    lastname = db.Column(db.String(40))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    gender = db.Column(db.String(6))
    biography = db.Column(db.String(1000))
    picture = db.Column(db.String(40))
    timestamp = db.Column(db.DateTime())
    
    # username = db.Column(db.String(80), unique=True)
    
    def __init__(self, firstname, lastname, email, location, gender, bio, fileName,timestamp):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = bio
        self.picture = fileName
        self.date = timestamp


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)