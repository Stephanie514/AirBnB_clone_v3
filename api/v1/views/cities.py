#!/usr/bin/python3
"""
Create a new view for City objects - handles all default RESTful API actions.
"""

from flask import abort, jsonify, request
<<<<<<< HEAD
from models.state import State
from models.city import City
from api.v1.views import app_views
from models import storage

=======
from models.state import State as CityState
from models.city import City as CityModel
from api.v1.views import app_views
from models import storage


>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities_by_state(state_id):
    """
    Retrieves the list of all City objects of a State.
    """
<<<<<<< HEAD
    state = storage.get(State, state_id)
    if not state:
        abort(404)

    cities = [city.to_dict() for city in state.cities]
    return jsonify(cities)
=======
    city_state = storage.get(CityState, state_id)
    if not city_state:
        abort(404)

    city_list = [city.to_dict() for city in city_state.cities]
    return jsonify(city_list)
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """
    Retrieves a City object.
    """
<<<<<<< HEAD
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())
=======
    city_obj = storage.get(CityModel, city_id)
    if city_obj:
        return jsonify(city_obj.to_dict())
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Deletes a City object.
    """
<<<<<<< HEAD
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
=======
    city_obj = storage.get(CityModel, city_id)
    if city_obj:
        storage.delete(city_obj)
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)

<<<<<<< HEAD
=======

>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """
    Creates a City object.
    """
<<<<<<< HEAD
    state = storage.get(State, state_id)
    if not state:
=======
    city_state = storage.get(CityState, state_id)
    if not city_state:
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

<<<<<<< HEAD
    data = request.get_json()
    if 'name' not in data:
        abort(400, 'Missing name')

    data['state_id'] = state_id
    city = City(**data)
    city.save()

    return jsonify(city.to_dict()), 201
=======
    city_data = request.get_json()
    if 'name' not in city_data:
        abort(400, 'Missing name')

    city_data['state_id'] = state_id
    city_obj = CityModel(**city_data)
    city_obj.save()

    return jsonify(city_obj.to_dict()), 201
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """
    Updates a City object.
    """
<<<<<<< HEAD
    city = storage.get(City, city_id)
    if city:
        if not request.get_json():
            abort(400, 'Not a JSON')

        data = request.get_json()
        ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(city, key, value)

        city.save()
        return jsonify(city.to_dict()), 200
=======
    city_obj = storage.get(CityModel, city_id)
    if city_obj:
        if not request.get_json():
            abort(400, 'Not a JSON')

        city_data = request.get_json()
        ignore_keys = ['id', 'state_id', 'created_at', 'updated_at']

        for key, value in city_data.items():
            if key not in ignore_keys:
                setattr(city_obj, key, value)

        city_obj.save()
        return jsonify(city_obj.to_dict()), 200
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
    else:
        abort(404)


@app_views.errorhandler(404)
def not_found(error):
    """
    404: Not Found.
    """
    return jsonify({'error': 'Not found'}), 404


@app_views.errorhandler(400)
def bad_request(error):
    """
    Return Bad Request message for illegal requests to API.
    """
    return jsonify({'error': 'Bad Request'}), 400
