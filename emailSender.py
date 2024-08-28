print("Starting the email script...")
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Email
EMAIL_ADDRESS = 'abcd@efgh.com'
EMAIL_PASSWORD = '########'

RECIPIENT_EMAIL = 'pqrs@dfgh.com'

def send_email(subject, body):
    print("Preparing to send email")
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS, RECIPIENT_EMAIL, text)
        print(f"Email sent to {RECIPIENT_EMAIL}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def payment_reminder():
    print("Calling payment_reminder function")
    subject = "Study Reminder"
    body = "Reminder to pay"
    send_email(subject, body)

# Schedule the time
schedule.every().day.at("00:00").do(payment_reminder) #change accordingly
print("Schedule set for 00:00")

while True:
    print("Checking schedule")
    schedule.run_pending()
    time.sleep(60)  