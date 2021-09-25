from typing import Text
from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms.fields.core import SelectField
from ..models import Comment, User



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class Blog_Form(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Write a Descritpion', validators=[Required()])
    submit = SubmitField('submit')

class Comment_Form(FlaskForm):
    Comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Submit')