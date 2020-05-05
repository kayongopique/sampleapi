from tests.test_base2 import BaseTestCase
import unittest
import json
from tests import app
import os

class EndTests(BaseTestCase):

    def test_cannot_fetch_all_orders_with_unauthorized_access(self):
        res = self.fetch_all_orders()
        self.assertEqual(res.status_code, 200)


    def test_can_fetch_all_orders_by_specific_user(self):
        self.make_valid_order()
        res = self.client.get( '/api/orders/worker/1', content_type='application/json',\
        headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)


    def test_cannot_fetch_all_orders_with_unauthorized_access(self):
        self.make_valid_order()
        res = self.client.get( '/api/orders', content_type='application/json',\
        headers={'Authorization': ""})
        self.assertEqual(res.status_code, 401)

    def test_cannot_make_invalid_order(self):
        response = self.client.post( '/api/orders',content_type='application/json',\
        headers={'Authorization': self.get_token()}, data=json.dumps({}))
        self.assertEqual(response.status_code, 400)
     

    def test_delete_worker(self):
        res = self.client.delete('/api/workers/1/delete', headers={'Authorization': self.get_token()})
        self.assertEqual(res.status_code, 200)

    
    def test_cannot_assign_sameorder_twice2worker(self):
        response = self.make_extra_orders()
        self.assertEqual(response.status_code, 400)


    def test_cannot_assign_morethan_five_orders_to_worker(self):
        response = self.make_extraof_five_orders()
        self.assertEqual(response.status_code, 400)
    