import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from datetime import datetime
import config

def send_email(report_path):
    sender_email = config.MAIL_USERNAME
    receiver_email = config.MAIL_TO_ADDRESS
    password = config.MAIL_PASSWORD
    cc_emails = config.MAIL_CC_ADDRESS


    subject = f"NIFTY50 Daily Report - {datetime.today().strftime('%Y-%m-%d')}"
    body = "Attached is the daily NIFTY50 stock market report."
    cc_emails = config.MAIL_CC_ADDRESS

    # Create message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = ", ".join(receiver_email)
    msg["Subject"] = subject
    msg["CC"] = ", ".join(cc_emails)
    msg.attach(MIMEText(body, "plain"))

    # Attach file
    with open(report_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(report_path)}")
        msg.attach(part)


    # Recipients list (To + CC)
    recipients = receiver_email + cc_emails

    # Send email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipients, msg.as_string())
        server.quit()
        print(f"Email sent successfully to {recipients}")
    except Exception as e:
        print(f"Error sending email: {e}")