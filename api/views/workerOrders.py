from flask import jsonify, request, json
from api.views import appblueprint, is_not_valid_order_key,\
is_not_valid_order, db_conn
from api.models.models import WorkOrder
from flask_jwt_extended import jwt_required,get_jwt_identity


@appblueprint.route('/orders', methods=['POST'])
@jwt_required
def assign_order():

    worker_identiy = get_jwt_identity()
    order_request = request.json
    if is_not_valid_order_key(order_request):
        return is_not_valid_order_key(order_request),400

    # if is_not_valid_order(order_request):
    #     return is_not_valid_order(order_request),400

    title = request.json.get('title')
    description= request.json.get('description')
    deadline = request.json.get('deadline')
    
    new_order = WorkOrder(title,description,worker_identiy['worker_id'], deadline)

    if len(db_conn.fetch_orders(new_order)["workerid"])>=5:
        return jsonify({"message":"worker order maximum limit reached"}),201
    db_conn.add_order(new_order) 
    order = db_conn.query_last_item()
    return jsonify({"message":"order added successfully","order":order}),201

@appblueprint.route('/orders', methods=['GET'])
@jwt_required
def fetch_all_orders():
    orders = db_conn.fetch_all_orders()
    newlist =[]
    for order in orders:
        worker_id = order["workerid"]
        name = db_conn.fetch_worker_by_id(worker_id)["name"]
        order["name"] = name
        newlist.append(order)  
    return jsonify({"orders":newlist}),200


@appblueprint.route('/worker/orders', methods=['GET'])
@jwt_required
def fetch_orders_by_specific_worker():
    worker_id = get_jwt_identity()['worker_id']
    orders = db_conn.fetch_specific_worker_orders(worker_id)
    print(orders)
    newlist=[]
    for order in orders:
        worker_id = order["workerid"]
        name = db_conn.fetch_worker_by_id(worker_id)["name"]
        order["name"] = name
        newlist.append(order)  
    return jsonify({"orders":newlist}),200

@appblueprint.route('/orders/<int:order_id>/delete', methods=['DELETE'])
@jwt_required
def delete_order(order_id):
    if not db_conn.fetch_order('orderId',order_id):
        return jsonify({"message":"order does not exist"}),404
        
    db_conn.delete('orders','orderId',order_id)
    return jsonify({"message":"successfully deleted"}),200


