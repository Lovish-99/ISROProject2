# importing the libraries
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import insertddl
from .models import insertgraph2
from django.contrib import messages
import csv
import folium
import pandas as pd
import time
from .locatemap import *
from .practical import *
from background_task.models import Task, CompletedTask
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from authentication import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token

# declare the count vriable globally
count = 10

#  declare home function 
def home(request):
    if request.method == "POST":
        if request.POST.get('pname') and request.POST.get('yesno'):
            savevalue=insertddl()
            savevalue.pname=request.POST.get('pname')
            savevalue.yesno=request.POST.get('yesno')
            savevalue.save()
            parameter = savevalue.pname
            val = savevalue.yesno 

            if val == "Site1A":
                context = locate_map1(parameter, val)
            elif val == "Site1B":
                context = locate_map2(parameter, val)
            elif val == "Site1C":
                context = locate_map3(parameter, val)
            else:
                context = locate_map4(parameter, val)

            #notifier()
            #returning the values that we want to represent in index1.html page
            return render(request, 'index1.html', context)
    else:
        #create a folium map 
        f = folium.Figure(height=517, width=934)
        #setting the location of a map for 'India'
        m = folium.Map(location=[22.9734, 78.6569], zoom_start=5).add_to(f)
        m = m._repr_html_()
        context = {'m' : m}
        return render(request, 'index1.html',context)

#  declare amount function 
def about(request):
    return render(request, 'about.html')

#  declare contact function 
def contact(request):
    return render(request, 'contact.html')

#  declare services function 
def services(request):
    if request.method == "POST":
        if request.POST.get('service1') and request.POST.get('service2') and request.POST.get('service3'):
            savevalue=insertgraph2()
            savevalue.service1=request.POST.get('service1')
            savevalue.service2=request.POST.get('service2')
            savevalue.service3=request.POST.get('service3')
            savevalue.save()
            g1  = savevalue.service1
            g2  = savevalue.service2
            g3  = savevalue.service3
            g4 = int(g3)
            if g1 == "Site1A":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            elif g1 == "Site1B":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime2/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            elif g1 == "Site1C":
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS/Runtime/{}/Location{}/Data.jpeg'".format(g2,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS/Runtime3/Location's.csv")
                d3=df5['Name Of The River'].tolist()
                g5 = d3[g4]
            else:
                g2a = g2.replace("/","_")
                g = "<img style='height:500px; width:1080px;' src='/static/RuntimeS1/{}/Location{}/Data.jpeg'".format(g2a,str(g4 + 1)) + "'>"
                df5=pd.read_csv("static/RuntimeS1/Location's.csv")
                d3=df5['Location'].tolist()
                g5 = d3[g4]
            context = {
                'g' : g,
                'g1' : g1,
                'g2' : g2,
                'g3' : g5
            }
            return render(request, 'services.html',context)
    else:
        return render(request, 'services.html')

def feedback(request):
    return render(request, 'feedback.html', {
        'room_name': "room_name",
    })
        
   
#  declare home function  
def room(request):
    return render(request, 'room.html', {
        'room_name': "room_name",
    })

#  declare signup function 
def signup(request):
    # check for the post request
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('room')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('room')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('room')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('room')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('room')
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        myuser.is_active = True
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('signin')  
    
    return render(request, "signup.html")

#  declare activate function 
def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')

#  declare signin function 
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            return render(request, "room.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('room')
    
    return render(request, "signin.html")

#  declare signout function 
# to logout from the site
def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('room')