import unittest
from src.subscription import subscribe_user, get_subscribed_projects

class TestSubscriptionManager(unittest.TestCase):
    def test_subscribe_user(self):
        subscribe_user("test@example.com", "Hello-World")
        self.assertIn("Hello-World", get_subscribed_projects("test@example.com"))

if __name__ == "__main__":
    unittest.main()
