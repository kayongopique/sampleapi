from api.models.db_controller import Dbcontroller
from flask import Blueprint,jsonify
from api.models.validators import Validator

appblueprint = Blueprint('api',__name__)


db_conn = Dbcontroller()
is_valid = Validator()


"""These functions below validate the json input data and return user friendly responses"""

def is_not_valid_signup_key_word(json_input):
    if is_not_valid_name_key_word(json_input):
        return is_not_valid_name_key_word(json_input)
    if not json_input.get('email'):
        return jsonify({"message":"email key word is not in the right format"})

def is_not_valid_name_key_word(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('name'):
        return jsonify({"message":"name key word is not in the right format"})
   

def is_not_valid_order_key(json_input):
    if not json_input:
        return jsonify({"message":"request must be in json format"})
    if not json_input.get('title'):
        return jsonify({"message":"title key word is not in the right format"})
    if not json_input.get('description'):
        return jsonify({"message":"description key word is not in the right format"})
   

def is_not_valid_worker_details(json_input):
        if not is_not_valid_worker_name_details(json_input):
                return is_not_valid_worker_name_details(json_input)
        if not is_valid.email(json_input.get('email')):
                return jsonify({"message":"email not in the right format"})

def is_not_valid_worker_name_details(json_input):
        if not is_valid.pure_text(json_input.get("name")):
                return jsonify({"message":"an error occured in name input"})
