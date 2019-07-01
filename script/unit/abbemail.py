import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(msgBody):
    msg = MIMEMultipart()
    msg["From"] = "data-au-bon-beurre@dany-corbineau.fr"
    msg["To"] = "danycor2@hotmail.fr"
    msg["Subject"] = "Au Bon Beurre - Error"
    msg.attach(MIMEText(msgBody, 'plain'))
    server = smtplib.SMTP("emailing",1025)
    #server = smtplib.SMTP("smtp.office365.com",587)
    #server.starttls()
    server.ehlo_or_helo_if_needed()
    #server.login("dany.corbineau@ynov.com", password)
    try:
        failed = server.sendmail("data-au-bon-beurre@dany-corbineau.fr","danycor2@hotmail.fr", msg.as_string())
        server.close()
    except Exception as e:
        print(e)