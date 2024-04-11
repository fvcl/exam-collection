from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired

# make db directory
os.makedirs('db', exist_ok=True)

app = Flask(__name__)
app.debug = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.secret_key = 'super secret'
app.config['UPLOAD_FOLDER'] = 'static/data'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'exco.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# get logger to write into gunicorn log
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


class UploadForm(FlaskForm):
    file = FileField('File', validators=[FileRequired()])
    uploader = StringField('Uploader Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    year = IntegerField('Year', default=2024)
    course = StringField('Course')
    has_solution = BooleanField('Has Solution')


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    uploader = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    course = db.Column(db.String(128), nullable=True)
    has_solution = db.Column(db.Boolean, nullable=False)


# Create the database tables
with app.app_context():
    db.create_all()


# Page Routes
@app.route('/')
def index():
    resources = Resource.query.all()  # Query all resources from the database
    return render_template('index.html', resources=resources)


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
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        resource = Resource(filename=filename, uploader=uploader, description=description, year=year, course=course,
                            has_solution=has_solution)
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
