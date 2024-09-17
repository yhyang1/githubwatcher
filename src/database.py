import sqlite3

DB_NAME = 'githubwatcher.db'

class Database:
    def __init__(self, db_name=DB_NAME):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # 创建 repositories 表
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS repositories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_name TEXT NOT NULL,
            owner_name TEXT NOT NULL,
            description TEXT,
            stars INTEGER,
            forks INTEGER,
            created_at TEXT,
            updated_at TEXT
        )
        ''')

        # 创建 commits 表
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS commits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repo_id INTEGER,
            commit_hash TEXT NOT NULL,
            author TEXT NOT NULL,
            message TEXT NOT NULL,
            commit_date TEXT,
            FOREIGN KEY (repo_id) REFERENCES repositories(id)
        )
        ''')

        # 创建 subscriptions 表
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT NOT NULL,
            repo_id INTEGER,
            FOREIGN KEY (repo_id) REFERENCES repositories(id)
        )
        ''')

        self.connection.commit()

    def insert_repository(self, repo_data):
        """插入 GitHub 项目数据到 repositories 表"""
        self.cursor.execute('''
        INSERT INTO repositories (repo_name, owner_name, description, stars, forks, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (repo_data['name'], repo_data['owner']['login'], repo_data['description'],
              repo_data['stargazers_count'], repo_data['forks_count'],
              repo_data['created_at'], repo_data['updated_at']))
        self.connection.commit()

    def insert_commit(self, repo_id, commit_data):
        """插入提交记录到 commits 表"""
        self.cursor.execute('''
        INSERT INTO commits (repo_id, commit_hash, author, message, commit_date)
        VALUES (?, ?, ?, ?, ?)
        ''', (repo_id, commit_data['sha'], commit_data['commit']['author']['name'],
              commit_data['commit']['message'], commit_data['commit']['author']['date']))
        self.connection.commit()

    def close(self):
        self.connection.close()