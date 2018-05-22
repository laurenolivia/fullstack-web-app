import server
import unittest

class IntegrationTestCase(unittest.Testcase):

    def test_home(self):
        """Test homepage"""

        #test_client() makes request to app
        client = server.app.test_client()
        result = client.get('/home')
        self.assertEqual(result.status_code, 200)


    def test_register_form(self):

        client = server.app.test_client()
        result = client.post('/register', data={})
        self.assertIn("Plese Register", result.data)

    def test_login_form(self):

        client = server.app.test_client()
        result = client.post('/login', data={})
        self.assertIn("LOGIN HERE", result.data)

    def test_user_account(self):
        
        client = server.app.test_client()
        result = client.get("user_account")
        self.assertIn("Enter Today's Data:", result.data)


# class FlaskClientTestCase(unittest.Testcase):
    
#     def SetUp(self):
#         pass

#     def TearDown(self):
#         pass





if __name__ == '__main__':
    unittest.main()        


