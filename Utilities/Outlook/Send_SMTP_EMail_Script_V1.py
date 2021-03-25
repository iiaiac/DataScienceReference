
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = """

<b> Your Message Goes Here </b>
"""

def send_mail(from_id, password, to, subject, message):
    smtp_server_dictionary = {'outlook.com':'smtp.office365.com','gmail.com':'smtp.gmail.com'}
    # create message object instance
    msg = MIMEMultipart()
    message = message

    # setup the parameters of the message
    password = password
    msg['From'] = from_id
    msg['To'] = to
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'html'))

    #create server
    server = smtplib.SMTP(smtp_server_dictionary.get(from_id[from_id.find('@')+1:].lower()) + ': 587')
    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

    print("successfully sent email to %s:" % (msg['To']))
    return 1

send_mail(from_id = 'xxxx', password = 'xxxx', to = 'Email_Address', subject = 'Thank you for sharing the details', message = message)

