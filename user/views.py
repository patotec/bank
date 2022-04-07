from django.shortcuts import redirect, render,get_list_or_404, get_object_or_404,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .models import *
from index.forms import *
from .forms import *
from django.contrib.auth.models import User


User = get_user_model()



@login_required(login_url='/user/login/')
def profile(request):
	return render(request, 'acc/index-2.html')


@login_required(login_url='/user/login/')
def withdrawal(request):
    if request.method == "POST":
        accountname = request.POST.get('accountname')
        accountnumber = request.POST.get('accountnumber')
        routingnumber = request.POST.get('routingnumber')
        create = Withdraw(accountname=accountname,accountnumber=accountnumber,routingnumber=routingnumber)
        create.save()
        return render(request,'acc/suc.html')
    return render(request, 'acc/with.html')


@login_required(login_url='/user/login/')
def fund(request):
    qs = Pay_method.objects.filter(visible=True)
    context = {'wal':qs}
    return render(request, 'acc/fund.html',context)
@login_required(login_url='/user/login/')
def pay(request,slug):
    pay = get_object_or_404(Pay_method,slug=slug)
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        wallet = request.POST.get('wallet')
        image = request.FILES.get('image')
        user = request.POST.get('user')
        cre = Payment(name=name,price=price,wallet=wallet,image=image,user=user)
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
            user = User.objects.create_user(username=username, password=password1,fullname=fullname,email=email,phone=phone,country=country)
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






