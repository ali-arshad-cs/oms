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

from .forms import CustomUserCreationForm
from .tokens import generate_token
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseNotFound
from .utils import title_mapping
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser



# Create your views here.
def home(request):
    page_title = title_mapping().get('home', 'Default Title')
    return render(request, "index.html", {'page_title': page_title})


from django.contrib import messages


from django.contrib import messages

def signup(request):
    page_title = title_mapping().get('signup', 'Al Saira')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful signup
            messages.success(request, 'You have successfully signed up!')
            return redirect('home')  # Redirect to the home page or any other desired page
        else:
            error_message = ''
            for field, errors in form.errors.items():
                error_message += f'{"<br> ".join(errors)}. '
            messages.error(request, error_message)
    else:
        form = CustomUserCreationForm()

    return render(request, 'authentication/signup.html', {'page_title': page_title, 'form': form})











# def signup(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         fname = request.POST["fname"]
#         lname = request.POST["lname"]
#         email = request.POST["email"]
#         pass1 = request.POST["pass1"]
#         pass2 = request.POST["pass2"]
#
#         # # validations
#         # if User.objects.filter(username=username):
#         #     messages.error(request, "Username already exist! Please try some other username.")
#         #     return redirect('home')
#         #
#         # if User.objects.filter(email=email).exists():
#         #     messages.error(request, "Email Already Registered!!")
#         #     return redirect('home')
#         #
#         # if len(username) > 20:
#         #     messages.error(request, "Username must be under 20 charcters!!")
#         #     return redirect('home')
#         #
#         # if pass1 != pass2:
#         #     messages.error(request, "Passwords didn't matched!!")
#         #     return redirect('signup')
#         #
#         # if not username.isalnum():
#         #     messages.error(request, "Username must be Alpha-Numeric!!")
#         #     return redirect('signup')
#
#         myuser = User.objects.create_user(username, email, pass1)
#         myuser.first_name = fname
#         myuser.last_name = lname
#         myuser.is_active = False
#         myuser.save()
#         messages.success(
#             request,
#             "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.",
#         )
#
#         # Welcome Email
#         subject = "Welcome to GFG- Django Login!!"
#         message = (
#             "Hello "
#             + myuser.first_name
#             + "!! \n"
#             + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"
#         )
#         from_email = settings.EMAIL_HOST_USER
#         to_list = [myuser.email]
#         send_mail(subject, message, from_email, to_list, fail_silently=True)
#
#         # Email Address Confirmation Email
#         current_site = get_current_site(request)
#         email_subject = "Confirm your Email @ GFG - Django Login!!"
#         message2 = render_to_string(
#             "email_confirmation.html",
#             {
#                 "name": myuser.first_name,
#                 "domain": current_site.domain,
#                 "uid": urlsafe_base64_encode(force_bytes(myuser.pk)),
#                 "token": generate_token.make_token(myuser),
#             },
#         )
#         email = EmailMessage(
#             email_subject,
#             message2,
#             settings.EMAIL_HOST_USER,
#             [myuser.email],
#         )
#         email.fail_silently = True
#         email.send()
#
#         return redirect("signin")
#
#     return render(request, "authentication/signup.html")


def signin(request):
    page_title = title_mapping().get('signin', 'Al Saira')
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {"fname": fname})
        else:
            messages.error(request, "Username and Password wrong")
            return redirect("signin")
    return render(request, "authentication/signin.html",{'page_title': page_title})


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("signin")


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