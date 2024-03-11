#!/usr/bin/python3
"""
Defines the views for the User object RESTful API actions
"""

from api.v1.views import app_views
from flask import jsonify, make_response, abort, request
from models import storage
from models.user import User as UserModel


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Retrieves the list of all User objects"""
    users_list = []
    users = storage.all("User")
    for user in users.values():
        users_list.append(user.to_dict())
    return jsonify(users_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieves a User object"""
    user_obj = storage.get(UserModel, user_id)
    if user_obj is None:
        abort(404)
    return jsonify(user_obj.to_dict())


@app_views.route("/users/<user_id>",
                 methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user_obj = storage.get(UserModel, user_id)
    if user_obj is None:
        abort(404)
    storage.delete(user_obj)
    storage.save()
    return make_response(jsonify({}))


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Creates a User"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'email' not in request.get_json():
        abort(400, 'Missing email')
    if 'password' not in request.get_json():
        abort(400, 'Missing password')
    user_data = request.get_json()
    user_obj = UserModel(**user_data)
    storage.new(user_obj)
    storage.save()
    return make_response(jsonify(user_obj.to_dict()), 201)


@app_views.route("/users/<user_id>", methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Updates a User object"""
    user_obj = storage.get(UserModel, user_id)
    if user_obj is None:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for key, value in request.get_json().items():
        if key not in ignore_keys:
            setattr(user_obj, key, value)
    storage.save()
    return make_response(jsonify(user_obj.to_dict()), 200)
