import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from project import mail


def save_picture(form_picture):
    # Generate a random filename to prevent naming conflicts
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # Resize the image using the Pillow library
    output_size = (125, 125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(picture_path)

    return picture_fn


def send_reset_email(user):
    # Generate a password reset token and send an email to the user
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    reset_url = url_for('reset_token', token=token, _external=True)
    message_body = f'''To reset your password, visit the following link:
{reset_url}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    msg.body = message_body
    mail.send(msg)
