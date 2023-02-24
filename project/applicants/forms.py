from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class ApplicationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=255)])
    phone = StringField('Phone', validators=[DataRequired(), Length(max=20)])
    resume = FileField('Resume', validators=[DataRequired()])
    submit = SubmitField('Submit')

