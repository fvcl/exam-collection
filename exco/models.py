try:
    from exco.extensions import db
except ImportError:
    from exco import db
import random


class Resource(db.Model):
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
