import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message




def save_picture(form_picture):
    # change the name of image with secrets
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    # con file name hex and ext
    picture_fn = random_hex + f_ext
    # adds the picture path to the static folder/profile_pics with file name
    # os module need to go through it 
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # pillow resizing interesting - look at it more 
    output_size = (125, 125)
    i = Image.open(form_picture)

    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


