from email.mime.multipart import MIMEMultipart
import smtplib, ssl #pip install secure-smtplib
import getpass
import schedule #pip install schedule
import time
import pymysql.cursors #pip install pymysql

#Definition of functions
def NotifyEmail():
    try:
        server.sendmail(username, notification, msg.as_string())
    finally:
        server.quit()

def ProbeDB():
        connnection = pymysql.connect(host='localhost',
                                     user='user',
                                     password='12345',
                                     database='db',
                                     cursorclass=pymysql.cursors.DictCursor)
        with connnection:
            try:
                with connnection.cursor() as cursor:
                    sql = "SELECT `users`"
                    cursor.execute(sql)
            except:
                NotifyEmail()
         
def sched_job():
     schedule.every(900).seconds.do(ProbeDB) #schedule job every 15 minutes
     return schedule.CancelJob

#User input
print("Welcome to the Database monitoring system DBMS.\nPlease login to the system email to begin the notification to the system")
username = input("Please enter your email:")
password = getpass.getpass(prompt = "Please enter your password:")
domain = input("Please enter your email domain:")
notification = input("Please enter the email that you would like to receive server notifications with:")
port = 465
context = ssl.create_default_context()

with smtplib.SMTP_SSL(domain, port, context=context) as server:
        server.login (username, password)

msg = MIMEMultipart('The database is currently down.')
msg['To'] = notification
msg['From'] = username
msg['Subject'] = 'Production database instance is currently not working'

schedule.every().day.at('00:00').do(sched_job)

while True:
     schedule.run_pending()
     time.sleep(1)


