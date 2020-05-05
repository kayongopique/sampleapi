import unittest
import json
from tests import app
from api.views import db_conn
import os



class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client():
            db_conn.create_tables()
            self.test_user1 = {"name":"admin","email":"admin@gmail.com",\
            "company":"cisco"}
            self.test_user2 = {"name":"margret","email":"mar@gmail.com",\
            "company":"cisco"}
            self.test_user3 = {"name":"caleb","email":"cal@gmail.com",\
            "company":"cisco"}
            self.test_order ={"title":"the office","description":"micheal",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order1 ={"title":"big bang theory","description":"sheldon copper",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order2 ={"title":"baby daddy","description":"danny",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order3 ={"title":"mum","description":"christy",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order4 ={"title":"daddy","description":"christy",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order5 ={"title":"bob","description":"christy",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order6 ={"title":"elite","description":"spanish",\
            "deadline":"2019-07-14", \
                "worker_name": "caleb", "worker_email": "cal@gmail.com"}
            self.test_order7 ={"title":"mordern family","description":"spanish",\
            "deadline":"2019-07-14", "worker_name": "margret", \
                "worker_email": "mar@gmail.com"}
            self.test_order8 ={"title":"bat man","description":"spanish",\
            "deadline":"2019-07-14", \
                "worker_name": "margret", "worker_email": "mar@gmail.com"}
            
            

    def tearDown(self):
        db_conn.drop_tables()

    def register_worker(self):
        response = self.client.post('/api/auth/signup',\
        data=json.dumps(self.test_user1),content_type='application/json' )

    def register_other_workers( self ):
        workers = [ self.test_user2, self.test_user3 ]
        for worker in workers:
            response = self.client.post('/api/auth/signup',\
            data=json.dumps( worker ),content_type='application/json' )


    def login_worker(self):
        return self.client.post('/api/auth/login',\
         data=json.dumps(self.test_user1),content_type='application/json')

    def get_token(self):
        self.register_worker()
        response = self.login_worker()
        data = json.loads(response.data.decode())
        return 'Bearer ' + data['token']
     

    def make_valid_order(self):
        self.register_other_workers()
        response = self.client.post( '/api/orders',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response

    def fetch_all_orders(self):
        response = self.client.get( '/api/orders', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response
   
    
    def make_extra_orders(self):
        self.register_other_workers()
        orders = [self.test_order, self.test_order]
        for order in orders:
            response = self.client.post( '/api/orders',content_type='application/json',\
            headers={'Authorization': self.get_token()}, data=json.dumps(order))
        return response

    def make_extraof_five_orders(self):
        self.register_other_workers()
        orders = [self.test_order, self.test_order1, self.test_order2,\
            self.test_order3, self.test_order4, \
                self.test_order5, self.test_order6]
        for order in orders:
            response = self.client.post( '/api/orders',content_type='application/json',\
            headers={'Authorization': self.get_token()}, data=json.dumps(order))
        return response