import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    
    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body = (
        f"Hi,\n\nThe workflow '{workflow_name}' failed for the repo '{repo_name}'.\n"
        f"Please check the logs for more details.\n\n"
        f"More Details:\nRun ID: {workflow_run_id}"
    )
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully ✅")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_mail(
        os.getenv('WORKFLOW_NAME'),
        os.getenv('REPO_NAME'),
        os.getenv('WORKFLOW_RUN_ID')
    )
