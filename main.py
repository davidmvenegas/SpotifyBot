import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    email_sender = 'spotifypodcastbot@gmail.com'
    email_password = 'jornxxaujitbnmsa'
    email_receiver = 'venegasdavidm@gmail.com'

    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = 'Spotify Podcast Bot'
    MESSAGE['From'] = email_sender
    MESSAGE['To'] = email_receiver

    with open('./email.html', 'r', encoding='utf-8') as html_file:
        BODY = html_file.read()

    HTML_BODY = MIMEText(BODY, 'html')
    MESSAGE.attach(HTML_BODY)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, MESSAGE.as_string())
    server.quit()

    print("email sent")

main()