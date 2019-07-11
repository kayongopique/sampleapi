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
            self.test_user1 = {"name":"david","email":"wali@gmail.com",\
            "company":"wrej@jafcd"}
            self.test_order ={"title":"the office","description":"micheal",\
            "deadline":"2019/07/14"}
            self.test_order1 ={"title":"big bang theory","description":"sheldon copper",\
            "deadline":"2019/07/14"}
            self.test_order2 ={"title":"baby daddy","description":"danny",\
            "deadline":"2019/07/14"}
            self.test_order3 ={"title":"mun","description":"christy",\
            "deadline":"2019/07/14"}
            self.test_order4 ={"title":"elite","description":"spanish",\
            "deadline":"2019/07/14"}
            
            

    def tearDown(self):
        db_conn.drop_tables()

    def register_worker(self):
        response = self.client.post('/api/auth/signup',\
        data=json.dumps(self.test_user1),content_type='application/json' )


    def login_worker(self):
        return self.client.post('/api/auth/login',\
         data=json.dumps(self.test_user1),content_type='application/json')

    def get_token(self):
        self.register_worker()
        response = self.login_worker()
        data = json.loads(response.data.decode())
        return 'Bearer ' + data['access_token']
     

    def make_valid_order(self):
        response = self.client.post( '/api/orders',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response

    def fetch_all_orders(self):
        response = self.client.get( '/api/orders', content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps(self.test_order))
        return response
   
    
    def make_extra_orders(self):
        orders = [self.test_order,self.test_order]
        for order in orders:
            response = self.client.post( '/api/orders',content_type='application/json',\
            headers={'Authorization': self.get_token()}, data=json.dumps(order))
        return response

    def make_extraof_five_orders(self):
        orders = [self.test_order,self.test_order,self.test_order,\
            self.test_order,self.test_order,self.test_order, self.test_order]
        for order in orders:
            response = self.client.post( '/api/orders',content_type='application/json',\
            headers={'Authorization': self.get_token()}, data=json.dumps(order))
        return response