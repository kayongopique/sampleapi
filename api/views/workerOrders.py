from flask import jsonify, request, json, g
from api.views import appblueprint, is_not_valid_order_key,\
db_conn
from api.models.models import WorkOrder, Worker
from flask_jwt_extended import jwt_required,get_jwt_identity
import datetime as dt
from functools import wraps


@appblueprint.before_request
@jwt_required
def do_before_each_request():
    workerId = get_jwt_identity()['worker_id']
    g.user = db_conn.fetch_worker_by_id(workerId)

def superuser( func ):
    @wraps( func )
    def decorator( *args, **kwargs ):
        if g.user['name'] != 'admin' \
            and g.user['email'] != 'admin@gmail.com':
            return jsonify({ "message": "Not authorized to perform this operation" }), 401
        return func( *args, **kwargs  )
    return decorator


@appblueprint.route('/orders', methods=['POST'])
@jwt_required
@superuser
def assign_order():
    order_request = request.json
    if is_not_valid_order_key(order_request):
        return is_not_valid_order_key(order_request),400
    title = request.json.get('title')
    description= request.json.get('description')
    date_time = request.json.get('deadline')
    name = request.json.get( 'worker_name' )
    email = request.json.get('worker_email')
    # fetch the worker
    current_worker = Worker( name, email, ' ')
    worker = db_conn.fetch_worker( current_worker )
    if worker is not None:
        deadline = dt.datetime.strptime(str(date_time), \
            "%Y-%m-%d").timestamp()
        
        new_order = WorkOrder( title, description, worker['workerid'], deadline)
        orders = db_conn.fetch_orders(new_order)
        if orders is not None:
            for order in orders:
                if order['workerid'] == worker['workerid']:
                    return jsonify({\
                        "message":"worker already assigned this work order"}),400
                else:
                    return jsonify( { \
                        "message": "work order already assigned "
                        } ), 400
        if len(db_conn.fetch_specific_worker_orders(worker['workerid'])) >= 5:
            return jsonify({"message":"worker order maximum limit reached"}),400
        db_conn.add_order(new_order) 
        order = db_conn.query_last_item()
        return jsonify({"message":"order added successfully","order":order}),201
    else:
        return jsonify({"message": "worker doesn't exist"})

@appblueprint.route('/orders', methods=['GET'])
@jwt_required
@superuser
def fetch_all_orders():
    orders = db_conn.fetch_all_orders()
    newlist = [ order for order in orders ]
    return jsonify({"orders":newlist}),200


@appblueprint.route('/orders/worker/<int:worker_id>', methods=['GET'])
@jwt_required
def fetch_orders_by_specific_worker(worker_id):
    worker_orders = db_conn.fetch_specific_worker_orders(worker_id)
    newlist = [ order for order in worker_orders ]
    return jsonify({"orders":newlist}),200


@appblueprint.route('/orders/<int:order_id>/delete', methods=['DELETE'])
@jwt_required
@superuser
def delete_order(order_id):
    if not db_conn.fetch_order('orderId',order_id):
        return jsonify({"message":"order does not exist"}),404
        
    db_conn.delete('orders','orderId',order_id)
    return jsonify({"message":"successfully deleted"}),200

@appblueprint.route('/workers/<int:worker_id>', methods=['GET'])
@jwt_required
def fetch_worker(worker_id):
    if not db_conn.fetch_worker_by_id(worker_id):
        return jsonify({"message":"order does not exist"}),404
    return jsonify({'worker' :db_conn.fetch_worker_by_id(worker_id) }),200


@appblueprint.route('/workers/<int:worker_id>/delete', methods=['DELETE'])
@jwt_required
@superuser
def delete_worker(worker_id):
    if not db_conn.fetch_worker_by_id(worker_id):
        return jsonify({"message":"order does not exist"}),404
        
    db_conn.delete('workers','workerid',worker_id)
    return jsonify({"message":"successfully deleted"}),200