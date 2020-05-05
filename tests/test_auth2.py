import unittest
from tests import app
from api.views import db_conn

class TestApi(unittest.TestCase):
    """
    Class inherits from unittest class. Used for testing app.
    """

    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        with self.app.test_client() as client:
           db_conn.create_tables()
           self.test_user1 = {"name":"admin","email":"admin@gmail.com",\
           "company":"cisco"}

    def tearDown(self):
        db_conn.drop_tables()

    def test_can_sign_up(self):
        response = self.client.post('/api/auth/signup', json = self.test_user1)
        self.assertIn('you have successfully signed up', str(response.data))
        self.assertEqual(response.status_code, 201)

    def test_invalid_sign_up_name_key(self):
        invalid_user = {"Naame":"wali","email":"wali@ymail.com",\
        "company":"1234"}
        response = self.client.post('/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('name key word is not in the right format', str(response.data))

    def test_invalid_sign_up_email_key(self):
        invalid_user = {"name":"david","Evmail":"kay@ymail.com",\
        "company":"1234"}
        response = self.client.post('/api/auth/signup', json = invalid_user)
        self.assertEqual(response.status_code, 400)
        self.assertIn('email key word is not in the right format', str(response.data))

   

    def test_invalid_json(self):
        self.client.post('/api/auth/signup', json = self.test_user1)
        response = self.client.post('/api/auth/login', json = {})
        self.assertEqual(response.status_code, 400)
       

    
    
