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
