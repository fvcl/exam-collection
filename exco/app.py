"""
This is the main application file for the Flask web application.
It initializes the Flask app, configures the database, and creates the database tables and imports the routes.
"""

import random
import os
from flask import Flask

try:
    from exco.extensions import db
    from exco.utils import format_date_info
except ImportError:
    from extensions import db
    from utils import format_date_info

app = Flask(__name__)
# Check if we are running in development mode
DEVELOPMENT_MODE = os.environ.get('DEVELOPMENT_MODE', True)
print(format_date_info("BOOT"),
      f"Development mode is set to {DEVELOPMENT_MODE}")

# Generic configuration
app.debug = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app.secret_key = random.randbytes(16)
app.config['UPLOAD_FOLDER'] = 'static/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['APPLICATION_ROOT'] = '/'

# Mode-specific configuration
if DEVELOPMENT_MODE is True:
    # Create the database directory if it doesn't exist
    os.makedirs('db', exist_ok=True)
    # Development mode configuration
    print(format_date_info("BOOT"), "Running in development mode with SQLite database.")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'db', 'exam-collection.db')
else:
    # Production mode configuration
    app.config['SERVER_NAME'] = 'exams.fvcl.ch'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['SESSION_COOKIE_SECURE'] = True
    print(format_date_info("BOOT"), "Running in production mode with PostgreSQL database.")
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ac69327d785a127a800e@diy-prod_exam-collection-db:5432/diy-prod'


# Initialize the database
db.init_app(app)

# Create the database tables (if they don't exist)
with app.app_context():
    # If the database is not created, create it
    db.create_all()
    print(format_date_info("BOOT"), "Created database tables (if they didn't exist yet).")

    # Import the routes (requires the active app context)
    try:
        import exco.routes
    except ImportError:
        import routes
    print(format_date_info("BOOT"), "Initialized routes.")




if __name__ == '__main__':
    app.run()
