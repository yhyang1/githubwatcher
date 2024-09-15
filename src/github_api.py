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
