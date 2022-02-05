import schedule
import time
import nmap, socket
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOSTNAME = ''

  
def func():

    
    
    hostname = HOSTNAME
    
    response = os.system("ping " + hostname)
    # and then check the response...
    if response == 0:
        
        pingstatus = "Network Active"
        print(pingstatus)
    else:
        pingstatus = "Network Error"
        print(pingstatus)
        mail_content = 'Server is Down'
        #The mail addresses and password
        sender_address = 'pkagwe07@gmail.com'
        sender_pass = 'kagwepeter07@gmail.com'
        receiver_address = 'towuor@gokhanmasterspacejv.co.ke'
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Alert!'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        
        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('mwandishi.co.ke', 80))
    if result == 0:
        print("Port is open")
    else:
        print("Port is not open")
  
schedule.every(0.05).minutes.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(0.05)

