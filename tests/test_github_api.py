import unittest
from src.github_api import fetch_github_repo_data

class TestGitHubAPI(unittest.TestCase):
    def test_fetch_github_repo_data(self):
        data = fetch_github_repo_data("octocat", "Hello-World")
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Hello-World")

if __name__ == "__main__":
    unittest.main()
