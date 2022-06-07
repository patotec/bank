from django.shortcuts import redirect, render,get_list_or_404, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import *
from index.forms import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str, force_text, DjangoUnicodeDecodeError
from .utils import generate_token
import threading
import string
import random


User = get_user_model()

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('acc/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMultiAlternatives(subject=email_subject, body=email_body, from_email=settings.EMAIL_HOST_USER,to=[user.email] )
    email.attach_alternative(email_body, "text/html")

    EmailThread(email).start()


@login_required(login_url='/user/login/')
def profile(request):
    qs = Tran.objects.all()
    context = {'qs':qs}
    return render(request, 'acc/index-2.html',context)

@login_required(login_url='/user/login/')
def loan(request):
    return render(request, 'acc/loan.html')

@login_required(login_url='/user/login/')
def withdrawal(request):
    if request.method == "POST":
        accountname = request.POST.get('accountname')
        accountnumber = request.POST.get('accountnumber')
        bankname = request.POST.get('bankname')
        email = request.POST.get('email')
        randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        cre = Withdraw.objects.create(accountname=accountname,accountnumber=accountnumber,bankname=bankname,pin=randompin)
        Otp.objects.create(otp=randompin, user=request.user)
        email_body = render_to_string('acc/mali.html', {
        'data':cre
        })
        msg = EmailMultiAlternatives(subject='Otp Request', body=email_body, from_email=settings.DEFAULT_FROM_EMAIL,to=[email] )
        msg.attach_alternative(email_body, "text/html")
        msg.send()
        return redirect('userurl:otp')
    return render(request, 'acc/with.html')

def otp(request):
    if request.method == "POST":
        otp = request.POST.get('otp')

        try:
            loadedpin = Otp.objects.get(otp=otp)
            checkactive = loadedpin.active
            if checkactive == True:
                messages.error(request, 'Pin already in use')
            else:
                loadedpin.active = True
                loadedpin.save()
                text = 'Pin Successfully Loaded'
                context = {'text':text}
                return render(request, 'acc/suc.html', context)
        except Otp.DoesNotExist:
            messages.error(request, 'Invalid Pin')
    return render(request,'acc/otp.html')

# @login_required(login_url='/user/login/')
# def fund(request):
#     qs = Pay_method.objects.filter(visible=True)
#     context = {'wal':qs}
#     return render(request, 'acc/fund.html',context)
@login_required(login_url='/user/login/')
def pay(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        user = request.POST.get('user')
        cre = Payment(image=image,user=user)
        cre.save()
        messages.success(request,'Your Payment will be Aproved in the next 24hrs...')
    context = {'data':pay}
    return render(request, 'acc/pay.html',context)



def signupView(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        image = request.FILES.get('image')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('userurl:signup')
        elif password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('userurl:signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Taken')
            return redirect('userurl:signup')
        else:
            randompin = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            user = User.objects.create_user(username=username, password=password1,fullname=fullname,email=email,phone=phone,country=country,image=image,accnumber=randompin)
            send_activation_email(user, request)
            messages.add_message(request, messages.SUCCESS,'We sent you an email to verify your account')
            return redirect('userurl:login')
    return render(request, 'acc/register.html')


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            newurl = request.GET.get('next')
            if newurl:
                return redirect(newurl)
            return redirect('userurl:profile')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {}
    return render(request, 'acc/login.html')

def logout_view(request):
	logout(request)
	return redirect('/user/login')

def activate_user(request, uidb64, token):

    try:
        uid = force_text(urlsafe_base64_decode(uidb64))

        user = User.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS,'Email verified, you can now login')
        return redirect('userurl:login')

    return render(request, 'acc/activate-failed.html', {"user": user})






