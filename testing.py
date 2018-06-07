import server
import unittest
from unittest import TestCase
from model import db, connect_to_db, example_data, User, Event, Type
import datetime
from server import app

class FlaskTestRoutes(TestCase):

    def setUp(self):
        """To do before every test"""

        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True
        app.config['SECRET KEY'] = 'thisisasecret'

        #Connect to testdb
        connect_to_db(app, "postgresql:///testdb")
        
        db.create_all()
        example_data()


    def tearDown(self):
        """To do after every test"""
        
        db.session.close()
        db.drop_all()
        

    def test_home(self):
        """Test homepage"""

        #test_client() makes request to app
        # client = server.app.test_client()
        result = self.client.get('/home')
        self.assertEqual(result.status_code, 200)


    def test_validate_user(self):

        # client = server.app.test_client()
        result = self.client.post('/validate_registration', 
            data={
            'First': 'Lauren', 
            'Last': 'Burwell',
            'Username': 'lburwell',
            'Password': 'lburwell'
            },
            follow_redirects=True)
        #should assertIn look for what new page renders?
        self.assertIn("An account with this username already exists", result.data)

    def test_create_user(self):

        result = self.client.post('/validate_registration', 
            data={
            'First': 'Jane', 
            'Last': 'Doe',
            'Username': 'jdoe',
            'Password': 'jdoe'
            },
            follow_redirects=True)

        self.assertIn("Please log in!", result.data)

    def test_login_form(self):

        # client = server.app.test_client()
        result = self.client.post('/login', data={'Username': 'lburwell', 
                                                'Password': 'lburwell'},
                                                    follow_redirects=True)
        self.assertIn("Have you pooped today?", result.data)

    def test_user_account(self):
        
        # client = server.app.test_client()
        result = self.client.get("/user_account", follow_redirects=True)
        self.assertIn("Not logged in", result.data)

    
    def test_submit_form(self):
        result = self.client.post("/user_account",
                              data={"type_id": 7,
                                    "comment": "lumpy, brown"},
                              follow_redirects=True)
        self.assertEqual(result.status_code, 200)                          


class DatabaseTests(TestCase):
    
    #special method; requires camelCase
    def setUp(self):
        """To do before every test"""
        
        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True
        app.config['SECRET KEY'] = 'thisisasecret'

        #Connect to testdb
        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()

        #only allow access to page if user is logged in
        with self.client as c:
            with c.session_transaction() as sess:
                sess['username'] = 'lburwell'
                sess['user_id'] = 1


    #special method; requires camelCase
    def tearDown(self):
        """To do after every test"""
        
        db.session.close()
        db.drop_all()

        



if __name__ == '__main__':  #pragma: no cover
    
    #runs all cases
    unittest.main()        


