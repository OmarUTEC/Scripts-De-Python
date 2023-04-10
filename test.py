# desarrollar un programa que permita enviar un correo electronico a un destinatario  con un archivo adjunto 

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = " "
toaddr = " "

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE MAIL"

body = "TEXT YOU WANT TO SEND"

msg.attach(MIMEText(body, 'plain'))

filename = "NAME OF THE FILE WITH ITS EXTENSION"
attachment = open("PATH OF THE FILE", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(fromaddr, "PASSWORD OF YOUR EMAIL")

text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()

# Path: test.py
# desarrollar un programa que permita enviar un correo electronico a un destinatario  con un archivo adjunto