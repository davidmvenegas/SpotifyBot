import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader, select_autoescape


def send_email(**email_variables):
    email_sender = 'spotifypodcastbot@gmail.com'
    email_password = 'atycuopjnosvuplc'
    email_receiver = 'venegasdavidm@gmail.com'

    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = 'Spotify Podcast Bot'
    MESSAGE['From'] = email_sender
    MESSAGE['To'] = email_receiver

    env = Environment(
        loader=FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('email.html')

    BODY = template.render(**email_variables)
    HTML_BODY = MIMEText(BODY, 'html')
    MESSAGE.attach(HTML_BODY)

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(email_sender, email_password)
    server.sendmail(email_sender, email_receiver, MESSAGE.as_string())
    server.quit()

    print("Email sent successfully")


def get_spotify_data():
    return {
        'saved_episodes': '44',
        'new_episodes': '99',
    }


def run_bot():
    data = get_spotify_data()
    print(data)

    # send_email(
    #     saved_episodes=data['saved_episodes'],
    #     new_episodes=data['new_episodes'],
    # )


run_bot()
