import requests
from src.config import Config
from src.database import Database

config = Config().get_github_config()

def fetch_github_repo_data(owner, repo):
    """获取 GitHub 项目数据并存储到数据库"""
    url = f"{config['api_url']}/repos/{owner}/{repo}"
    headers = {'Authorization': f"token {config['access_token']}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repo_data = response.json()
        db = Database()
        db.insert_repository(repo_data)  # 存储项目信息到数据库
        db.close()
        return repo_data
    else:
        raise Exception(f"Failed to fetch data for {repo}: {response.status_code}")

def fetch_repo_commits(owner, repo):
    """获取项目的提交记录并存储到数据库"""
    url = f"{config['api_url']}/repos/{owner}/{repo}/commits"
    headers = {'Authorization': f"token {config['access_token']}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        commit_data = response.json()
        db = Database()
        repo_info = fetch_github_repo_data(owner, repo)
        repo_id = repo_info['id']
        for commit in commit_data:
            db.insert_commit(repo_id, commit)  # 存储提交记录到数据库
        db.close()
    else:
        raise Exception(f"Failed to fetch commits for {repo}: {response.status_code}")