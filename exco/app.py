import random
import os
from flask import Flask

try:
    from exco.extensions import db
    from exco.forms import UploadForm
    from exco.models import Resource
    from exco.utils import format_date_info
except ImportError:
    from extensions import db
    from forms import UploadForm
    from models import Resource
    from utils import format_date_info

app = Flask(__name__)
# Check if we are running in development mode
DEVELOPMENT_MODE = os.environ.get('DEVELOPMENT_MODE', True)
print(format_date_info("BOOT"),
      f"Development mode is set to {DEVELOPMENT_MODE}")

# make directories
os.makedirs('db', exist_ok=True)
os.makedirs('static/data', exist_ok=True)

# Create the Flask app

app.debug = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.secret_key = random.randbytes(16)
app.config['UPLOAD_FOLDER'] = 'static/data'

if DEVELOPMENT_MODE is not True:
    # Production mode configuration
    app.config['SERVER_NAME'] = 'exams.fvcl.ch'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['APPLICATION_ROOT'] = '/'
    app.config['SESSION_COOKIE_SECURE'] = True

# Configure the database
if DEVELOPMENT_MODE is True:
    print(format_date_info("BOOT"),
          "Running in development mode with SQLite database.")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'exam-collection.db')
else:
    print(format_date_info("BOOT"),
          "Running in production mode with PostgreSQL database.")
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ac69327d785a127a800e@diy-prod_exam-collection-db:5432/diy-prod'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize the database
db.init_app(app)

# Create the database tables (if they don't exist)
with app.app_context():
    db.create_all()
    print(format_date_info("BOOT"), "Created database tables.")
    try:
        import exco.routes
    except ImportError:
        import routes
    print(format_date_info("BOOT"), "Initialized routes.")




if __name__ == '__main__':
    app.run()
