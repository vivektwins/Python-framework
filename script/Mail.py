#import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os,glob


fromaddr = "vivekkumam26@gmail.com"
toaddr = "vivekkumarn28@gmail.com,vivek.k@hashedin.com"

# instance of MIMEMultipart
msg = MIMEMultipart()

# storing the senders email address
msg['From'] = fromaddr

# storing the receivers email address
msg['To'] = toaddr

# Multi user
msg["Cc"] = ""

# storing the subject
msg['Subject'] = "Sending mail with attachments"

# string to store the body of the mail
body = "Sending the report to multiple users"

# attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))


#Finding the Html file and attaching the file.

folder_path = 'C://Users/Hasher/PycharmProjects/StumpNew/'
for filename in glob.glob(os.path.join(folder_path, '*.html')):
  with open(filename, 'r') as f:
    print(filename)
    last = os.path.basename(filename)
    print(last)

if last is not None:
    attachment =open(filename)
    print(attachment)

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % last)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "5353798942")

    #send a mail to Multiple users
    s.sendmail(msg["From"], msg['To'].split(","), msg.as_string())

    # terminating the session
    s.quit()


else:
    print("Sorry, Expected file was not there in that folder")
