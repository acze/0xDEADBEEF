import unittest
import web

class DeadbeefTestCase(unittest.TestCase):
    def setUp(self):
        self.app = web.app.test_client()

    def test_index(self):
        response = self.app.get('/')
        assert b'mail' in response.data

if __name__ == '__main__':
    unittest.main()
