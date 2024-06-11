#!/usr/bin/python3
<<<<<<< HEAD
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places_amenities import *
=======
'''
This Creates a Blueprint instance with `url_prefix` set to `/api/v1`.
'''
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
<<<<<<< HEAD
from api.v1.views.index import *
from api.v1.views.cities import *
=======

from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.users import *
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
from api.v1.views.states import *
>>>>>>> 5f13e6cd59cb591c5fe7a4b2477ab188fb762915
