from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length

class JobForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    company = StringField('Company', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=500)])
    location = StringField('Location', validators=[DataRequired(), Length(max=100)])
    salary_min = DecimalField('Minimum Salary', validators=[DataRequired()])
    salary_max = DecimalField('Maximum Salary', validators=[DataRequired()])
