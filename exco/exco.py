from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os, time
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired
try:
    from exco.ftp_sync import send_file_to_ftp_server, get_files_from_ftp_server
except ImportError:
    from ftp_sync import send_file_to_ftp_server, get_files_from_ftp_server


# make directories
os.makedirs('db', exist_ok=True)
os.makedirs('static/data', exist_ok=True)

app = Flask(__name__)
app.debug = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.secret_key = 'super secret'
app.config['UPLOAD_FOLDER'] = 'static/data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ac69327d785a127a800e@diy-prod_exam-collection-db:5432/diy-prod'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    uploader = StringField('Uploader Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    year = IntegerField('Year', default=2024)
    course = StringField('Course')
    has_solution = BooleanField('Has Solution')
    resource_type_choices = ['Exam', 'Summary', 'Homework', 'Cheat Sheet', 'Other']
    resource_type = SelectField('Resource Type', choices=resource_type_choices, validators=[DataRequired()])


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    uploader = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    course = db.Column(db.String(128), nullable=True)
    has_solution = db.Column(db.Boolean, nullable=False)
    resource_type = db.Column(db.String(128), nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


# Page Routes
@app.route('/')
def index():
    selected_course = request.args.get('course')
    if selected_course:
        resources = Resource.query.filter_by(course=selected_course).all()
    else:
        resources = Resource.query.all()

    # Query all distinct courses for the filter dropdown
    courses = Resource.query.with_entities(Resource.course).distinct().all()
    courses = [c[0] for c in courses]  # Convert list of tuples to list of strings

    # add "resource_age" field containing the number of years since the resource was released
    for resource in resources:
        resource.age = time.localtime().tm_year - resource.year

    return render_template('index.html', resources=resources, courses=courses, selected_course=selected_course, types=UploadForm.resource_type_choices)



@app.route('/upload', methods=['GET', 'POST'])
def upload_page():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        uploader = form.uploader.data
        description = form.description.data
        filename = file.filename
        year = form.year.data
        course = form.course.data
        has_solution = form.has_solution.data
        resource_type = form.resource_type.data
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # save file to FTP server
        send_file_to_ftp_server(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'], filename))
        resource = Resource(filename=filename, uploader=uploader, description=description, year=year, course=course,
                            has_solution=has_solution, resource_type=resource_type)
        db.session.add(resource)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


@app.route('/file/<int:file_id>')
def file_details(file_id):
    resource = Resource.query.get_or_404(file_id)  # Fetch the specific file or return 404
    return render_template('file_details.html', resource=resource)


if __name__ == '__main__':
    app.run()
