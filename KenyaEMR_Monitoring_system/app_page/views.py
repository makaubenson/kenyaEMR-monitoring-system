
from django.shortcuts import render
import schedule
import time
import os
import nmap, socket
from django.http import HttpResponse
import datetime
from django.contrib import messages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
checks = []

def home(request):
    if request.method == 'POST':
        hostname = request.POST.get('address')
        checks1 = checks
        def func():

            response = os.system("ping " + hostname)
            # and then check the response...
            if response == 0:
                pingstatus = "Network Active"
                checks.append(pingstatus)
                print(pingstatus)
                messages.add_message(request, messages.INFO, 'Hello world.')
            else:
                pingstatus = "Network Error"
                print(pingstatus)
                checks.append(pingstatus)
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
                print('Mail Sent'
            now = datetime.datetime.now()
            html = "<html><body>It is now %s.</body></html>" % now
            return HttpResponse(html)      

        schedule.every(0.05).minutes.do(func)
        while True:
           schedule.run_pending()
           time.sleep(0.05)

    return render(request, 'app_page/home.html')



