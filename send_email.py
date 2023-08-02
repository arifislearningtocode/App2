import smtplib
import ssl
import os


def send_email(message):
    host = 'smtp.gmail.com'
    port = 456

    username = 'coolabdulrehman3030@gmail.com'
    password = os.getenv("PASSWORD")
    # password = 'igpuipazijglmxep'

    receiver = 'coolabdulrehman3030@gmail.com'
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
