import server
import unittest
from unittest import Testcase
from model import db, connect_to_db, example_data, User, Event, Type
import datetime


class FlaskTestRoutes(Testcase):

    def SetUp(self):
        """To do before every test"""

        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True
        app.config['SECRET KEY'] = 'thisisasecret'

        #Connect to testdb
        connect_to_db(app, "postgresql:///testdb")

        db.create_all()
        example_data()


    def TearDown(self):
        """To do after every test"""
        
        db.session.close()
        db.drop_all()
        

    def test_home(self):
        """Test homepage"""

        #test_client() makes request to app
        client = server.app.test_client()
        result = client.get('/home')
        self.assertEqual(result.status_code, 200)


    def test_register_form(self):

        client = server.app.test_client()
        result = client.post('/register', data={'first': 'Lauren', 'last': 'Burwell',
                                                'username': 'lburwell',
                                                    'password': 'lburwell'},
                                                        follow_redirects=True)
        #should assertIn look for what new page renders?
        self.assertIn("Please Register", result.data)

    def test_login_form(self):

        client = server.app.test_client()
        result = client.post('/login', data={'username': 'lburwell', 
                                                'password': 'lburwell'},
                                                    follow_redirects=True)
        self.assertIn("You are logged in.", result.data)

    def test_user_account(self):
        
        client = server.app.test_client()
        result = client.get("user_account")
        self.assertIn("Enter Today's Data:", result.data)


class DatabaseTests(Testcase):
    
    def SetUp(self):
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


    def TearDown(self):
        """To do after every test"""
        
        db.session.close()
        db.drop_all()

        



if __name__ == '__main__':  #pragma: no cover
    
    #runs all cases
    unittest.main()        


