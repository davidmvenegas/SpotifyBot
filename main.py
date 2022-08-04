from email.message import EmailMessage
from multiprocessing import context
import smtplib
import ssl

email_sender = 'spotifypodcastbot@gmail.com'
email_password = 'jornxxaujitbnmsa'
email_reciver = 'venegasdavidm@gmail.com'

subject = "TEST SUBJECT"
body = """
    THIS IS A TEST BODY
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())