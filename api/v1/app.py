#!/usr/bin/python3
"""
This module sets up a basic Flask application for the HBNB API.
"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


# Create an instance of the Flask class for our web app
app = Flask(__name__)

# Configure CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Register the blueprint 'app_views' to the Flask app instance
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage on teardown.
    This function will be executed after each request, ensuring that the
    storage is properly closed and resources are released.
    """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Not found"}), 404



if __name__ == "__main__":
    # Set host and port from environment variables or default to 0.0.0.0:5000
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask app
    app.run(host=host, port=port, threaded=True)
