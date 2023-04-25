import smtplib ,ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "harshg75@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "harshg75@gmail.com"
    context1 = ssl.create_default_context()

    with smtplib.SMTP_SSL(host,port, context=context1) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

