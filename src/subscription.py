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
