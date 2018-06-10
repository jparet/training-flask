# coding: utf-8

import os
import secrets

from PIL import Image

from flask import current_app, url_for
from flask_mail import Message

from flaskblog import mail


def save_picture(form_picture):
    """Minimaze then save picture of user profiles into the database."""
    random_hex = secrets.token_hex(8)
    (_, extension) = os.path.splitext(form_picture.filename)
    picture = random_hex + extension
    picture_path = os.path.join(current_app.root_path,
                                'static/profile_pics', picture)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture


def send_reset_email(user):
    """Send an email with instructions to reset user password."""
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f"""
    To reset your password, visit the following link:
    {url_for('users.reset_token', token=token, _external=True)}

    If you did not make this request,
    Then simply ignore this email and no changes will be made.
    """
    mail.send(msg)
