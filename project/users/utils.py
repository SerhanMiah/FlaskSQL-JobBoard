from io import BytesIO
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from project import mail
import cloudinary
import cloudinary.uploader



def save_picture(form_picture):
    # Generate a random filename to prevent naming conflicts
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # Upload the image to Cloudinary
    result = cloudinary.uploader.upload(form_picture, public_id=picture_fn, folder='profile_pics')

    # Resize the image if necessary
    try:
        output_size = (250, 250)
        i = Image.open(form_picture)
        i.thumbnail(output_size)
        # Generate a new filename for the resized image
        resized_fn = random_hex + '_resized' + f_ext
        resized_path = os.path.join(current_app.root_path, 'static/profile_pics', resized_fn)
        # Save the resized image
        i.save(resized_path)
        return resized_fn
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None





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
