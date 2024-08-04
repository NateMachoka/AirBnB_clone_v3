#!/usr/bin/python3

"""
This module initializes the 'views' package for the HBNB API.
"""
from flask import Blueprint

# Create a Blueprint instance for the API views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Import all views from the index module
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
