# coding: utf-8

from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import (DataRequired, Length, Email,
                                EqualTo, ValidationError)

from flaskblog.models import User


class LoginForm(FlaskForm):
    """Manage forms to log users into the app."""
    # FIELDS TO SUBMIT
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    # SUBMIT BUTTON
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """Manage forms to register users into the app."""
    # FIELDS TO SUBMIT
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    # SUBMIT BUTTON
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Check if the username is not already taken."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.\n'
                                  'Please choose another one.')

    def validate_email(self, email):
        """Check if the email is not already taken."""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken.\n'
                                  'Please choose another one.')


class RequestResetForm(FlaskForm):
    """Manage forms to request to reset user passwords."""
    # FIELDS TO SUBMIT
    email = StringField('Email', validators=[DataRequired(), Email()])
    # SUBMIT BUTTON
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        """Check if the email exists."""
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email.\n'
                                  'You must register first.')


class ResetPasswordForm(FlaskForm):
    """Manage forms to reset user passwords."""
    # FIELDS TO SUBMIT
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    # SUBMIT BUTTON
    submit = SubmitField('Reset Password')


class UpdateAccountForm(FlaskForm):
    """Manage forms to update user accounts."""
    # FIELDS TO SUBMIT
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Udate Profile Picture',
                        validators=[FileAllowed(['jpg', 'png'])])
    # SUBMIT BUTTON
    submit = SubmitField('Update')

    def validate_username(self, username):
        """Check if the username is not already taken."""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken.\n'
                                      'Please choose another one.')

    def validate_email(self, email):
        """Check if the email is not already taken."""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken.\n'
                                      'Please choose another one.')
