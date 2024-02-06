#!/usr/bin/python3
"""
Create a new view for City objects - handles all default RESTful API actions.
"""

from flask import abort, jsonify, request
from models.state import State as CityState
from models.city import City as CityModel
from api.v1.views import app_views
from models import storage


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def get_cities_by_state(state_id):
    """
    Retrieves the list of all City objects of a State.
    """
    city_state = storage.get(CityState, state_id)
    if not city_state:
        abort(404)

    city_list = [city.to_dict() for city in city_state.cities]
    return jsonify(city_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """
    Retrieves a City object.
    """
    city_obj = storage.get(CityModel, city_id)
    if city_obj:
        return jsonify(city_obj.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Deletes a City object.
    """
    city_obj = storage.get(CityModel, city_id)
    if city_obj:
        storage.delete(city_obj)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def create_city(state_id):
    """
    Creates a City object.
    """
    city_state = storage.get(CityState, state_id)
    if not city_state:
        abort(404)

    if not request.get_json():
        abort(400, 'Not a JSON')

    city_data = request.get_json()
    if 'name' not in city_data:
        abort(400, 'Missing name')

    city_data['state_id'] = state_id
    city_obj = CityModel(**city_data)
    city_obj.save()

    return jsonify(city_obj.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """
    Updates a City object.
    """
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
