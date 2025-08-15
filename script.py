import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name, workflow_run_id):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    subject = f"Workflow {workflow_name} completed for repo {repo_name}"
    body = (
        f"Hi,\n\n"
        f"The workflow '{workflow_name}' has completed for the repository '{repo_name}'.\n"
        f"More Details:\nRun_ID: {workflow_run_id}\n\n"
        f"Regards,\nGitHub Actions Bot"
    )

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully ✅")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_mail(
        os.getenv('WORKFLOW_NAME'),
        os.getenv('REPO_NAME'),
        os.getenv('WORKFLOW_RUN_ID')
    )
