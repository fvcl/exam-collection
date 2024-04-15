from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired


class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    uploader = StringField('Uploader Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    year = IntegerField('Year', default=2024)
    course = StringField('Course')
    has_solution = BooleanField('Has Solution')
    solution_filename = FileField('Solution')
    resource_type_choices = ['Exam', 'Summary', 'Homework', 'Cheat Sheet', 'Other']
    resource_type = SelectField('Resource Type', choices=resource_type_choices, validators=[DataRequired()])
