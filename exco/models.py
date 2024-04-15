try:
    from exco.extensions import db
except ImportError:
    from extensions import db
import random


class Resource(db.Model):
    """
    Defines a study resource that has been uploaded to the database
    Fields:
    - id: the unique identifier for the resource
    - filename: the name of the file uploaded
    - uploader: the name of the user who uploaded the file
    - description: a description of the resource
    - year: the year the resource was created (*not* the year it was uploaded)
    - course: the course the resource is related to
    - has_solution: a boolean indicating if the resource has a solution file
    - solution_filename: the name of the solution file, if it exists
    - resource_type: the type of resource (e.g., exam, summary, homework)

    The __repr__ method and the generate_dummy_resource method are used for testing and debugging purposes, mainly
    in cli.py.
    """
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(128), nullable=False)
    uploader = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(256), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    course = db.Column(db.String(128), nullable=True)
    has_solution = db.Column(db.Boolean, nullable=False)
    solution_filename = db.Column(db.String(128), nullable=True)
    resource_type = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<Resource {self.id}: {self.filename} by {self.uploader} ({self.course}, {self.year})>"

    @classmethod
    def generate_dummy_resource(cls):
        return cls(filename='.exists', uploader='mockuser', description='mock description',
                   year=random.randint(1990, 2024), course='mockcourse', has_solution=True, resource_type='Exam')
