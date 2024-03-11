#!/usr/bin/python3
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
