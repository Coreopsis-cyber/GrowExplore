from django.shortcuts import render
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
##from django.views.decorator import csrf_exempt
##from rest_framework.parsers import JSONParser
##from django.http.response import JsonResponse

from Login.models import Users


def homepage(request):
	return render(request, 'homepage.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/main/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form}) ##redirects to login

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		##StreakForm = NewStreakForm(request.POST)
		if form.is_valid():
			user = form.save()
			##if StreakForm.is_valid():
			  ##  StreakForm.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
##	StreakForm = NewStreakForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


