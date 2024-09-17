import unittest
from unittest.mock import patch
from src.scheduler import scheduled_job

class TestScheduler(unittest.TestCase):

    @patch('src.scheduler.fetch_github_repo_data')  # 修正路径，指向 scheduler 模块中使用的 fetch_github_repo_data
    @patch('src.scheduler.fetch_repo_commits')      # 修正路径，指向 scheduler 模块中使用的 fetch_repo_commits
    def test_scheduled_job(self, mock_fetch_commits, mock_fetch_repo_data):
        # 模拟 GitHub API 的返回值
        mock_fetch_repo_data.return_value = {
            'name': 'Hello-World',
            'stargazers_count': 1500
        }

        # 调用 scheduled_job 函数
        result = scheduled_job()

        # 验证是否正确抓取数据并返回
        self.assertEqual(result['name'], 'Hello-World')
        self.assertEqual(result['stargazers_count'], 1500)

        # 验证 fetch_repo_commits 被调用
        mock_fetch_commits.assert_called_with("octocat", "Hello-World")  # 确保 fetch_repo_commits 函数调用了预期的参数

if __name__ == "__main__":
    unittest.main()