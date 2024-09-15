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
