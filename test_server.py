import server
import unittest

class IntegrationTests(unittest.Testcase):

    def test_home(self):
        """Test homepage"""

        #test_client() makes request to app
        client = server.app.test_client()
        result = client.get('/home')
        self.assertEqual(result.status_code, 200)


    def test_register_form(self):

        client = server.app.test_client()
        result = client.post('/register', data={'first': 'Lauren', 'last': 'B',
                                                'username': 'lburwell',
                                                    'password': 'lburwell'},
                                                        follow_redirects=True)
        self.assertIn("Plese Register", result.data)

    def test_login_form(self):

        client = server.app.test_client()
        result = client.post('/login', data={'username': 'lburwell', 
                                                'password': 'lburwell'},
                                                    follow_redirects=True)
        self.assertIn("LOGIN HERE", result.data)

    def test_user_account(self):
        
        client = server.app.test_client()
        result = client.get("user_account")
        self.assertIn("Enter Today's Data:", result.data)


class DumpsDatabaseTests(unittest.Testcase):
    
    def SetUp(self):
        """To do before every test"""
        #Get the Flask test client
        self.client = app.test_client()

        #Show Flask errors that happen during tests
        app.config['TESTING'] = True

        #Connect to test db
        connect_to_db(app, "postgresql:///dumps")


    def TearDown(self):
        """To do after every test"""
        
        db.session.close()
        db.drop_all()

        




if __name__ == '__main__':
    unittest.main()        


