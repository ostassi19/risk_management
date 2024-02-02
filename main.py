from flask import Flask
from swagger_api import api_v1  # Import the Blueprint from your swagger module
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy with the Flask app
db.init_app(app)

# Register the Swagger Blueprint
app.register_blueprint(api_v1)

if __name__ == '__main__':
    # Create database tables on application startup
    with app.app_context():
        db.create_all()

    # Run the Flask application
    app.run(debug=True)
