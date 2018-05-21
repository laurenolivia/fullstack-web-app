import server
import unittest

class IntegrationTestCase(unittest.Testcase):

    def test_home(self):
        """Test homepage"""

        client = server.app.test_client()
        result = client.get('/home')

        self.assertIn("Sign Me Up!", result.data)


    def test_register(self):
        pass


