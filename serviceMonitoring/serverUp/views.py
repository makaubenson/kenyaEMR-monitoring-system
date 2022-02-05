from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import logout
from django import forms



import schedule
import time
import os
import nmap, socket
from django.http import HttpResponse
import datetime
from django.contrib import messages




# def home(request):
    

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html',{})
#register user
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(login_request)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


#user login
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
    return render(request, 'home.html')


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, "You are now logged in as {username}.")
                return redirect (dashboard)
            else:
                messages.error(request,"Invalid username or password.")
    else:
        messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="index.html", context={"login_form":form})

#logout
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect(login_request)


# # check server status.
def server(status):
    return render(status,'isUp.html',{})
