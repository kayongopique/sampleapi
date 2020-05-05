from api.views import db_conn, is_not_valid_name_key_word, \
is_not_valid_signup_key_word, is_not_valid_worker_details
from flask import jsonify, request, json
from flask_jwt_extended import create_access_token, jwt_required
from api.views import authblueprint
from api.models.models import Worker


@authblueprint.route('/auth/signup', methods=['POST'])
def addworker():
    """{"Name":"","Email":"","Company":""}"""
    user_input = request.json
    if is_not_valid_signup_key_word(user_input):
        return is_not_valid_signup_key_word(user_input),400

    if is_not_valid_worker_details(user_input):
        return is_not_valid_worker_details(user_input),400

    name = request.json.get('name', None)
    email = request.json.get('email', None)
    company = request.json.get('company', None)

    new_worker = Worker(name,email,company)

    if db_conn.fetch_worker(new_worker):
        return jsonify({"message":"worker already exists with this credentials"}),400

    db_conn.add_worker(new_worker)
    return jsonify({"message":"you have successfully signed up as"+ " " + new_worker.name}),201


@authblueprint.route('/auth/login', methods=['POST'])
def login():

    user_input = request.json
    if is_not_valid_name_key_word(user_input):
        return is_not_valid_name_key_word(user_input),400

    if is_not_valid_worker_details(user_input):
        return is_not_valid_worker_details(user_input),400

    name = request.json.get('name', None)
    email = request.json.get('email', None)

    new_worker = Worker(name,email,' ')
    current_worker = db_conn.fetch_worker(new_worker)
    if not current_worker:
        return jsonify({"message":"user does not exist, do you want to signup"}),404

    if current_worker['email'] != email:
        return jsonify({"message":"wrong credetials"}),400
    worker = {"worker_id":current_worker["workerid"]}

    access_token = create_access_token(identity=worker)
    return jsonify({'token':access_token,'message':'successfully logged in'}), 200



