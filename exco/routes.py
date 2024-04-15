from flask import render_template, request, redirect, url_for
import time
try:
    from exco.extensions import db
    from exco.forms import UploadForm
    from exco.models import Resource
    from exco.utils import format_date_info
    from exco.app import app
except ImportError:
    from extensions import db
    from forms import UploadForm
    from models import Resource
    from utils import format_date_info
    from app import app


# Page Routes
@app.route('/')
def index():
    print(format_date_info("REQS"), f"Index Page Requested from {request.user_agent}")
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

    return render_template('index.html', resources=resources, courses=courses, selected_course=selected_course,
                           types=UploadForm.resource_type_choices)


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
        solution_file = form.solution_filename.data
        solution_filename = solution_file.filename if solution_file else None
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        if solution_file:
            solution_file.save(os.path.join(app.config['UPLOAD_FOLDER'], solution_filename))
        resource = Resource(filename=filename, uploader=uploader, description=description, year=year, course=course,
                            has_solution=has_solution, resource_type=resource_type, solution_filename=solution_filename)
        db.session.add(resource)
        db.session.commit()
        print(format_date_info("REQS"), f"Uploaded file '{filename}' by '{uploader}' from ({request.user_agent})")
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


@app.route('/file/<int:file_id>')
def file_details(file_id):
    resource = Resource.query.get_or_404(file_id)  # Fetch the specific file or return 404
    return render_template('file_details.html', resource=resource)
