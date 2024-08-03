#!/usr/bin/python3

"""
This module defines the index route for the HBNB API.
"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def get_status():
    """Returns the status of the API.
    This endpoint returns a JSON object indicating that the API is running
    and available.

    Returns:
        A JSON response with a single key-value pair: {"status": "OK"}
    """
    return jsonify({"status": "OK"})
