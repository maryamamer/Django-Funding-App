from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import user
from projects.models import Project
from .forms import RegisterForm, LoginForm, UpdateProfile
from projects.forms import ProjectForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import re
import uuid
from datetime import datetime
from django.core.mail import send_mail



def home(request):
    return render(request, 'index.html')

def Registration(request):
    if request.method == "POST":
        code = uuid.uuid4()
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            savedForm = form.save()
            savedForm.code = code
            savedForm.save()
            fname=request.POST['fname']
            email = request.POST['email']
            password = request.POST['password']
            User.objects.create_user(username=fname, email=email, password=password)

            send_mail(
                'hello activate here',
                f"Welcome to our website activate here  http://localhost:8000/activate/{code}",
                'maryam@gmail.com',
                [savedForm.email],
                fail_silently=False,
            )
            return redirect('/login')

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def activate(request, activeno):
    # print(User.objects.filter(code=activeno))
    user_obj = user.objects.filter(code=activeno)
    if user_obj:
        user_obj = user_obj[0]
        # user_obj.state = 'A'
        if user_obj.datetime.date() == datetime.today().date():
            user_obj.save()
        else:
            user_obj.delete()
            return HttpResponse("<h1>your account has been deleted because u activate it late plz create new one <br>"
                                "<hr>"
                                "<h2>via this link ---->></h2><hr><hr>"
                                '<a href="http://localhost:8000/login">#login Here </a>')

        return HttpResponse("<h1>Activation Done <a href="
                            "http://localhost:8000/login"
                            ">#Click _to login now with your data</a></h1>")
    else:
        return HttpResponse("<h1>your account has been deleted because u activate it late plz create new one <br>.."
                            "<hr>"
                            "<h2>via this link ---->></h2><hr><hr>"
                            '<a href="http://localhost:8000/login">#login Here </a>')


def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            useremail = request.POST['email']
            mail=str(useremail)
            print(mail)
            username=mail.split('@')[0]
            print(username)

            password = request.POST['password']
            # authuser = authenticate(request, username=username, password=password)
            l_user = user.objects.filter(email=useremail, password=password)

            if l_user:
                l_user = l_user[0]
                request.session['email'] = useremail
                request.session['id'] = l_user.id
                request.session['name'] = l_user.fname
                return redirect('/home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def mylogout(request):
    logout(request)
    return redirect('/login')

def profile(request):
    if 'id' in request.session:
        User = user.objects.get(id=request.session['id'])
        return render(request, 'profile.html', {'users': User})
    else:
        return redirect('/login')


def Update_Profile(request):
    email = request.session['email']
    User = user.objects.get(email=email)
    if request.method == 'GET':
        form = UpdateProfile(
            initial={
                "fname": User.fname,
                "lname": User.lname,
                "phone": User.phone,
                "image": User.image,
                "date_birth": User.date_birth,
                "facebook_link": User.facebook_link,
                "country": User.country,
            })
        context = {"form": form}
        return render(request, "updateProfile.html", context=context)
    elif request.method == "POST":
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            email = request.session['email']
            User = user.objects.get(email=email)
            form = UpdateProfile(request.POST, request.FILES, instance=User)
            form.save()
            return redirect('/profile')
        else:
            form = UpdateProfile()
        return render(request, 'updateProfile.html', {'form': form})

def userproject(request):
    email=request.session['email']
    myuser=user.objects.get(email=email)
    id=myuser.id
    project =Project.objects.filter(user_id=id)
    print(Project.user_id)
    return render (request,'user_project.html',{'projects':project})




