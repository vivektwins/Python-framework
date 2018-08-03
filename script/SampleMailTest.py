
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "vivekkumam26@gmail.com"
toaddr = "vivekkumarn28@gmail.com,vivek.k@hashedin.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "SUBJECT OF THE EMAIL"

body = "TEXT YOU WANT TO SEND"

msg.attach(MIMEText(body, 'plain'))

filename = "C://Users/Hasher/PycharmProjects/StumpNew/report.html"
attachment = open(r'C://Users/Hasher/PycharmProjects/StumpNew/report.html')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)



server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "5353798942")
server.sendmail(msg["From"], msg['To'].split(","), msg.as_string())
#text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
server.quit()