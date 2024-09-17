import yaml
import os

class Config:
    def __init__(self, config_file='config.yaml'):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_github_config(self):
        return {
            'api_url': self.config.get('github', {}).get('api_url'),
            'access_token': os.getenv('GITHUB_TOKEN')  # 从环境变量读取 GitHub 令牌
        }

    def get_smtp_config(self):
        return {
            'server': self.config.get('smtp', {}).get('server'),
            'port': self.config.get('smtp', {}).get('port'),
            'username': os.getenv('SMTP_USERNAME'),  # 从环境变量读取 SMTP 用户名
            'password': os.getenv('SMTP_PASSWORD'),  # 从环境变量读取 SMTP 密码
            'from_email': self.config.get('smtp', {}).get('from_email')
        }

    def get_scheduler_config(self):
        return self.config.get('scheduler', {})

# 示例调用
if __name__ == "__main__":
    config = Config()
    print(config.get_github_config())
    print(config.get_smtp_config())
    print(config.get_scheduler_config())
