from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
import time
from django.apps import apps
from django.contrib.auth.decorators import login_required
from .models import Profile,Narayana_Question,Chaithanya_Question,Narayana_Submission,Chaithanya_Submission
import random
from django.core import serializers
import csv, io
import json
from .forms import SignUpForm,SaveForm
import urllib
from django import template
from collections import OrderedDict

global all_objects
all_objects=[]

# Create your views here.
def rand(n,x = 6):
	a = []
	while(x!=0):
		f = random.randrange(1,n+1)
		if f not in a:
			a.append(f)
			x-=1
	return a

def about_us_page(request,*args,**kwargs):
	return render(request,"about.html",{})

def index_page(request,*args,**kwargs):
	return render(request,"index.html",{})

def contact_page(request,*args,**kwargs):
	return render(request,"contact.html",{})

def logout_page(request,*args,**kwargs):
	messages.add_message(request, messages.INFO, f"Thank you {request.user.username} for logging out. See you soon....")
	logout(request)
	return redirect("/home")
	
def home_page(request,*args,**kwargs):
	return render(request,"home.html",{})

def countdown_page(request,*args,**kwargs):
	return render(request,"countdown.html",{})	

def sub_page(request):
	schoolname = request.user.profile.school_name
	app_models = apps.get_app_config('question').get_models()
	for model in app_models:
		if schoolname+"_Submission" in str(model):
			s = model
	if request.method == 'POST':
		form = SaveForm(request.POST)
		username = request.user.username
		data = request.POST["data"]
		score = request.POST["score"]
		time = request.POST["time"]
		x = len(s.objects.all())
		s.objects.create(name=username,data=json.loads(data,object_pairs_hook=OrderedDict),score=score,time=time)
		context = {
			'score' : score,
			'time' : time,
		}
		return render(request,"submit.html",context)
	return render(request,"submit.html",{})

@login_required(login_url="/login")
def result_page(request,*args,**kwargs):
	schoolname = request.user.profile.school_name
	app_models = apps.get_app_config('question').get_models()
	for model in app_models:
		if schoolname+"_Submission" in str(model):
			s = model
	name = request.user.username
	g = s.objects.filter(name=name)
	context = {
		'res' : g,
	}
	return render(request,"result.html",context)

	
@login_required(login_url="/login")
def quiz_page(request,*args,**kwargs):
	all_objects = []
	schoolname = request.user.profile.school_name
	app_models = apps.get_app_config('question').get_models()
	for model in app_models:
		if schoolname+"_Question" in str(model):
			all_object = len(model.objects.all())
			x = rand(all_object)
			for k in x:
				s = model.objects.get(id=k)
				all_objects.append(s)
	context = {
		'school' : schoolname,
		'questions' : all_objects,
	}
	return render(request,"quiz.html",context)

@login_required(login_url="/login")
def exam_page(request,*args,**kwargs):
	return render(request,"exam.html",{})

@csrf_protect
def login_page(request,*args,**kwargs):
	if request.method == 'POST':
		form = AuthenticationForm(request,request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user.is_superuser:
				return redirect('/admin')
			elif user.profile.role=="College-admin":
				request.session["sch"]=user.profile.school_name
				login(request, user)
				return redirect('/signup')
			elif user is not None:
				messages.add_message(request, messages.INFO, f"Welcome {username}. Write exam well....")
				login(request, user)
				return redirect('/exam')
			else:
				messages.error(request, "Invalid username or password.")
				return redirect('/login')
		else:
			messages.error(request, "Invalid username or password.")
			return redirect('/login')
	form = AuthenticationForm()
	return render(request,"login.html",{"form":form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.school_name = request.session["sch"]
            user.profile.role = 'Student'
            user.save()
            raw_password = form.cleaned_data.get('password1')
            messages.info(request, 'Account created successfully.....')
            return redirect('/signup')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})