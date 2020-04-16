from flask_wtf import FlaskForm
from wtforms import Form, StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class Profile(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField ('Gender', choices=[('Male','Male'),('Female','Female')], validators=[DataRequired()])
    email = StringField('E-mail', validators= [Email(), DataRequired()])
    location = StringField('Located at', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired(), 
      Length(min=15, max=200, message="Can enter from 15 to 200 characters.")
    ]) 
    
    picture = FileField('Image', 
    validators=[
        FileRequired("You need a profile pic."), 
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    submit = SubmitField("Add Profile") 
    
    