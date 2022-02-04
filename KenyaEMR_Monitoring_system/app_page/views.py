
from django.shortcuts import render
import schedule
import time
import os
import nmap, socket
from django.http import HttpResponse
import datetime
from django.contrib import messages
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
                
                
        """ sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('irc.myserver.net', 6667))
            if result == 0:
                portstatus = "Port is open"
                print(portstatus)
                checks.append(portstatus)
            else:
                portstatus = "Port is not open"
                print(portstatus)
                checks.append(portstatus)
            now = datetime.datetime.now()
            html = "<html><body>It is now %s.</body></html>" % now
            return HttpResponse(html) """
        schedule.every(0.05).minutes.do(func)
        
        while True:
            schedule.run_pending()
            time.sleep(0.05)

    return render(request, 'app_page/home.html')