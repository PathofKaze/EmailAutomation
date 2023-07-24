from email.mime.multipart import MIMEMultipart
import smtplib, ssl
import getpass

print("Welcome to the Database monitoring system DBMS.\nPlease login to the system email to begin the notification to the system")
username = input("Please enter your email:")
password = getpass.getpass(prompt = "Please enter your password:")
domain = input("Please enter your email domain:")
notification = input("Please enter the email that you would like to receive server notifications with:")
port = 465
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login (username, password)

msg = MIMEMultipart('The database is currently down.')
msg['To'] = notification
msg['From'] = username
msg['Subject'] = 'Production database instance is currently not working'

try:
    server.sendmail(username, notification, msg.as_string())
finally:
    server.quit()


