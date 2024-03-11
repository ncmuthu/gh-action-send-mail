import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email content
subject = 'Hello from GitHub Actions'
body = 'This is a test email sent from GitHub Actions.'
sender_email = input('Enter sender email: ')
receiver_email = input('Enter receiver email: ')

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
message.attach(MIMEText(body, "plain"))

# Send email
with smtplib.SMTP(input('Enter SMTP server: '), int(input('Enter SMTP port: '))) as server:
    server.starttls()
    server.login(input('Enter SMTP username: '), input('Enter SMTP password: '))
    server.sendmail(sender_email, receiver_email, message.as_string())

print('Email sent successfully!')
