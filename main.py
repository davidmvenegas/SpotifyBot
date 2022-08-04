import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('venegasdavidm@gmail.com', 's3cureP@ssw0rd')