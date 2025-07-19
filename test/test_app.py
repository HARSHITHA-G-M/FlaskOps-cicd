import unittest
import json
from app import app  # Import the Flask app instance

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Create a test client before each test."""
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the CI/CD Flask App!", response.data)

    def test_health_check(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"OK", response.data)

    def test_add_numbers(self):
        response = self.app.get("/add?a=5&b=10")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 15)

    def test_subtract_numbers(self):
        response = self.app.get("/subtract?a=20&b=5")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 15)

    def test_multiply_numbers(self):
        response = self.app.post("/multiply",
                                 data=json.dumps({"a": 5, "b": 6}),
                                 content_type="application/json")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 30)

    def test_divide_numbers(self):
        response = self.app.post("/divide",
                                 data=json.dumps({"a": 10, "b": 2}),
                                 content_type="application/json")
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["result"], 5.0)

    def test_divide_by_zero(self):
        response = self.app.post("/divide",
                                 data=json.dumps({"a": 10, "b": 0}),
                                 content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Division by zero", response.data)


if __name__ == "__main__":
    unittest.main()

