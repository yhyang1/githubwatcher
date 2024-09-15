import unittest
from src.scheduler import scheduled_job

class TestScheduler(unittest.TestCase):
    def test_scheduled_job(self):
        data = scheduled_job()
        self.assertIsNotNone(data)
        self.assertIn("id", data)

if __name__ == "__main__":
    unittest.main()
