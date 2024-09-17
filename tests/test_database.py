import unittest
import sqlite3
from src.database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(db_name='test_githubwatcher.db')

    def test_insert_repository(self):
        repo_data = {
            'name': 'Hello-World',
            'owner': {'login': 'octocat'},
            'description': 'This is a test repository',
            'stargazers_count': 100,
            'forks_count': 50,
            'created_at': '2023-01-01T00:00:00Z',
            'updated_at': '2023-01-01T00:00:00Z'
        }
        self.db.insert_repository(repo_data)

        # 检查是否插入成功
        self.db.cursor.execute('SELECT * FROM repositories WHERE repo_name = "Hello-World"')
        result = self.db.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Hello-World')

    def tearDown(self):
        self.db.connection.close()
        # 删除测试数据库文件
        import os
        os.remove('test_githubwatcher.db')

if __name__ == "__main__":
    unittest.main()