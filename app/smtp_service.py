import smtplib
from config import settings
from email.mime.text import MIMEText
from email.header import Header


def send_email_smtp(to, subject, message):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = settings.STMP_USERNAME
    smtp_password = settings.STMP_PASSWORD

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        mime = MIMEText(message, 'plain', 'utf-8')
        mime['Subject'] = Header(subject, 'utf-8')
        server.sendmail(smtp_username, to, mime.as_string())
