#!/usr/bin/python3
<<<<<<< HEAD
"""State view module for the API"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage, State


@app_views.route('/states', methods=['GET'])
def get_states():
    states_apilist = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(states_apilist)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    state_api = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
=======
"""
Create a new view for State objects - handles all default RESTful API actions.
"""

from flask import jsonify, request
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    storage.delete(state)
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
    storage.save()
    return jsonify({})


<<<<<<< HEAD
@app_views.route('/states', methods=['POST'])
def create_state():
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, description="Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if not request.is_json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
=======
@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"}), 404
    if not request.is_json:
        return jsonify({"error": "Not a JSON"}), 400
    data = request.get_json()
    ignore_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignore_keys:
>>>>>>> 3963fb6d1610fadaa1f58ff09ea437c727695207
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict())
