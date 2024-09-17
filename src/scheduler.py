from apscheduler.schedulers.blocking import BlockingScheduler
from src.github_api import fetch_github_repo_data,fetch_repo_commits
from src.config import Config

scheduler_config = Config().get_scheduler_config()

def scheduled_job():
    """定时任务：获取项目数据并存储到数据库"""
    repo_data = fetch_github_repo_data("octocat", "Hello-World")
    print(f"Data collected: {repo_data['name']} with {repo_data['stargazers_count']} stars")
    fetch_repo_commits("octocat", "Hello-World")
    return repo_data

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_job, 'interval', hours=scheduler_config['interval_hours'])
    scheduler.start()
