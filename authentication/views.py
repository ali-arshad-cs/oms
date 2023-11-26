from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import views
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, 'Your Account Successfully Created')
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = User.first_name
            return render(request, "authentication/index.html", {'fname': fname})
        else:
            messages.error(request, "Username and Password wrong")
            return redirect('signup')
    return render(request, "authentication/signin.html")


def signout(request):
    pass
