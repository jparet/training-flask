# coding: utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    """Manage forms to create new posts."""
    # FIELDS TO SUBMIT
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    # SUBMIT BUTTON
    submit = SubmitField('Post')
