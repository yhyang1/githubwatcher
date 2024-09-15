import unittest
from src.notification import send_email_notification

class TestEmailNotification(unittest.TestCase):
    def test_send_email_notification(self):
        result = send_email_notification("test@example.com", "Test", "This is a test.")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
