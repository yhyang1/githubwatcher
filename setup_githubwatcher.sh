#!/bin/bash

# 创建项目的根目录及其子目录
mkdir -p GitHubWatcher/src
mkdir -p GitHubWatcher/tests

# 在 GitHubWatcher 目录下创建 config.yaml 配置文件
cat <<EOL > GitHubWatcher/config.yaml
github:
  api_url: "https://api.github.com"
  access_token: "your_github_token"

smtp:
  server: "smtp.example.com"
  port: 587
  username: "yourusername"
  password: "yourpassword"
  from_email: "youremail@example.com"

scheduler:
  interval_hours: 1
EOL

echo "config.yaml created."

# 创建 src/config.py 文件
cat <<EOL > GitHubWatcher/src/config.py
import yaml

class Config:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_github_config(self):
        return self.config.get('github', {})

    def get_smtp_config(self):
        return self.config.get('smtp', {})

    def get_scheduler_config(self):
        return self.config.get('scheduler', {})

# 示例调用
if __name__ == "__main__":
    config = Config()
    print(config.get_github_config())
    print(config.get_smtp_config())
    print(config.get_scheduler_config())
EOL

echo "config.py created."

# 创建 src/github_api.py 文件
cat <<EOL > GitHubWatcher/src/github_api.py
import requests
from src.config import Config

config = Config().get_github_config()

def fetch_github_repo_data(owner, repo):
    url = f"{config['api_url']}/repos/{owner}/{repo}"
    headers = {'Authorization': f"token {config['access_token']}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data for {repo}: {response.status_code}")
EOL

echo "github_api.py created."

# 创建 src/scheduler.py 文件
cat <<EOL > GitHubWatcher/src/scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from src.github_api import fetch_github_repo_data
from src.config import Config

scheduler_config = Config().get_scheduler_config()

def scheduled_job():
    data = fetch_github_repo_data("octocat", "Hello-World")
    print("Data collected:", data)

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_job, 'interval', hours=scheduler_config['interval_hours'])
    scheduler.start()
EOL

echo "scheduler.py created."

# 创建 src/notification.py 文件
cat <<EOL > GitHubWatcher/src/notification.py
import smtplib
from email.mime.text import MIMEText
from src.config import Config

smtp_config = Config().get_smtp_config()

def send_email_notification(to_email, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = smtp_config['from_email']
    msg['To'] = to_email

    with smtplib.SMTP(smtp_config['server'], smtp_config['port']) as server:
        server.login(smtp_config['username'], smtp_config['password'])
        server.sendmail(smtp_config['from_email'], to_email, msg.as_string())
    return True
EOL

echo "notification.py created."

# 创建 src/report_generator.py 文件
cat <<EOL > GitHubWatcher/src/report_generator.py
from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'GitHub Project Report', 0, 1, 'C')

    def project_data(self, project_name, data):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, f'Project: {project_name}', 0, 1)
        for key, value in data.items():
            self.cell(0, 10, f'{key}: {value}', 0, 1)

def generate_report(project_name, data):
    pdf = PDFReport()
    pdf.add_page()
    pdf.project_data(project_name, data)
    pdf.output(f'{project_name}_report.pdf')
EOL

echo "report_generator.py created."

# 创建 src/subscription.py 文件
cat <<EOL > GitHubWatcher/src/subscription.py
subscriptions = {}

def subscribe_user(user_email, project_name):
    if user_email not in subscriptions:
        subscriptions[user_email] = []
    subscriptions[user_email].append(project_name)

def get_subscribed_projects(user_email):
    return subscriptions.get(user_email, [])

# 示例调用
subscribe_user("user@example.com", "Hello-World")
print(get_subscribed_projects("user@example.com"))
EOL

echo "subscription.py created."

# 创建测试用例文件
cat <<EOL > GitHubWatcher/tests/test_config.py
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
EOL

echo "test_config.py created."

# 创建其他测试用例文件
cat <<EOL > GitHubWatcher/tests/test_github_api.py
import unittest
from src.github_api import fetch_github_repo_data

class TestGitHubAPI(unittest.TestCase):
    def test_fetch_github_repo_data(self):
        data = fetch_github_repo_data("octocat", "Hello-World")
        self.assertIn("id", data)
        self.assertEqual(data["name"], "Hello-World")

if __name__ == "__main__":
    unittest.main()
EOL

echo "test_github_api.py created."

cat <<EOL > GitHubWatcher/tests/test_scheduler.py
import unittest
from src.scheduler import scheduled_job

class TestScheduler(unittest.TestCase):
    def test_scheduled_job(self):
        data = scheduled_job()
        self.assertIsNotNone(data)
        self.assertIn("id", data)

if __name__ == "__main__":
    unittest.main()
EOL

echo "test_scheduler.py created."

cat <<EOL > GitHubWatcher/tests/test_notification.py
import unittest
from src.notification import send_email_notification

class TestEmailNotification(unittest.TestCase):
    def test_send_email_notification(self):
        result = send_email_notification("test@example.com", "Test", "This is a test.")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
EOL

echo "test_notification.py created."

cat <<EOL > GitHubWatcher/tests/test_report.py
import unittest
from src.report_generator import generate_report
import os

class TestReportGenerator(unittest.TestCase):
    def test_generate_report(self):
        generate_report("TestProject", {"Stars": 100, "Forks": 50})
        self.assertTrue(os.path.exists("TestProject_report.pdf"))

if __name__ == "__main__":
    unittest.main()
EOL

echo "test_report.py created."

cat <<EOL > GitHubWatcher/tests/test_subscription.py
import unittest
from src.subscription import subscribe_user, get_subscribed_projects

class TestSubscriptionManager(unittest.TestCase):
    def test_subscribe_user(self):
        subscribe_user("test@example.com", "Hello-World")
        self.assertIn("Hello-World", get_subscribed_projects("test@example.com"))

if __name__ == "__main__":
    unittest.main()
EOL

echo "test_subscription.py created."

echo "GitHubWatcher project structure created successfully."