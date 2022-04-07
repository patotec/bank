from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, request
from user.models import Plan

def myindex(request):
    qs = Review.objects.all()
    ho = Plan.objects.all()
    context = {'rev':qs,'plan':ho}
    return render(request, 'index/index-3.html',context)


def mycontact(request):
	if request.method == 'POST':
		form = Contactform(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Thanks for your message we will repyl you shortly')
			
	else:
		form = Contactform()
	return render(request, 'index/contact.html')


def myabout(request):
	return render(request, 'index/about-us.html')

def myprivate(request):
	return render(request, 'index/privacy-policy.html')