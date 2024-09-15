import unittest
from src.config import Config

class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config()

    def test_github_config(self):
        github_config = self.config.get_github_config()
        self.assertIn('api_url', github_config)
        self.assertIn('access_token', github_config)

    def test_smtp_config(self):
        smtp_config = self.config.get_smtp_config()
        self.assertEqual(smtp_config['port'], 587)
        self.assertIn('server', smtp_config)

    def test_scheduler_config(self):
        scheduler_config = self.config.get_scheduler_config()
        self.assertEqual(scheduler_config['interval_hours'], 1)

if __name__ == "__main__":
    unittest.main()
