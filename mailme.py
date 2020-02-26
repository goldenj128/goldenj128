import smtplib, ssl

smtp_server = "smtp.mail.yahoo.com"
port = 465  # For starttls
sender_email = "golduino@yahoo.com"
password = "nxnxpmnxlubutubj"
receiver_email = "jonathangolden450@gmail.com"
message = """\
Subject: This message is sent from Python.

import smtplib, ssl

smtp_server = "smtp.mail.yahoo.com"
port = 465  # For starttls
sender_email = "golduino@yahoo.com"
password = "nxnxpmnxlubutubj"
receiver_email = "jonathangolden450@gmail.com"
message = <message here>

# Try to log in to server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

"""

# Try to log in to server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)