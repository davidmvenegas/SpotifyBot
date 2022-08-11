from email.message import EmailMessage
from multiprocessing import context
from datetime import datetime
import schedule
import smtplib
import time
import ssl

def main():
    email_sender = 'spotifypodcastbot@gmail.com'
    email_password = 'jornxxaujitbnmsa'
    email_reciver = 'venegasdavidm@gmail.com'

    now = datetime.now()
    time = (now.strftime("%I:%M%p"))

    subject = "TEST SUBJECT"
    body = """
        THIS IS A TEST BODY
        Sent at {time}
    """.format(time=time)

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_reciver, em.as_string())
        print("message sent")

    return

schedule.every().day.at("08:00").do(main)

while True:
    schedule.run_pending()
    print('waiting...')
    time.sleep(5)