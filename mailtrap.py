import smtplib
import getpass

login = input("Please enter your username:")
password = getpass.getpass(prompt:"Please enter your password:")
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login(login , password)
    server.sendmail(sender, receiver, message)
