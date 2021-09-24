import smtplib
import socket


gmail_user = 'putyourmailhere@gmail.com'
gmail_password = 'putyourpasswordhere'

sent_from = gmail_user
to = ['putyourmailhere0@gmail.com']
subject = 'SENDING EMAILS WITH PYTHON'
body = "This email was sent using a python script lol"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Good Job!')
except:
    print('Error!!! Try again')
