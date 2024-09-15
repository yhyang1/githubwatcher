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
