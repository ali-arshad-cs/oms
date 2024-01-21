from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from oms import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout

from orphans.views import get_orphan_stats
from .forms import CustomUserCreationForm
from .tokens import generate_token
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseNotFound
from .utils import title_mapping
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


def home(request):
    page_title = title_mapping().get('home', 'Default Title')
    orphan_stats = get_orphan_stats()

    return render(request, "index.html", {
        'page_title': page_title,
        **orphan_stats,
    })


def signup(request):
    if request.user.is_authenticated:
        return redirect("authentication:home")
    page_title = title_mapping().get('signup', 'Al Saira')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful signup
            messages.success(request, 'You have successfully signed up!')
            return redirect('authentication:home')  # Redirect to the home page or any other desired page
        else:
            error_message = ''
            for field, errors in form.errors.items():
                error_message += f'{"</br> ".join(errors)}. '
            messages.error(request, error_message)
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/signup.html', {'page_title': page_title, 'form': form})


def signin(request):
    # Check if the user is already logged in
    if request.user.is_authenticated:
        return redirect("authentication:home")  # Redirect to the home page if the user is already logged in

    page_title = title_mapping().get('signin', 'Al Saira')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["pass1"]
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(
                "authentication:home")  # Redirect to the home page or any desired page after successful login
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "authentication/signin.html", {'page_title': page_title})


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("authentication:signin")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect("signin")
    else:
        return render(request, "activation_failed.html")


def custom_404(request, exception=None):
    if request.path.startswith(settings.STATIC_URL):
        return HttpResponseNotFound()

    return render(request, '404.html', status=404)