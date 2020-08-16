from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User

# Create your views here.
from .models import *
from .forms import *
from .filters import *
from .decorators import *

@login_required(login_url='login')
def home(request):
	schemes = Scheme.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_schemes = schemes.count()

	context = {'schemes':schemes, 'customers':customers,
	'total_schemes':total_schemes}
	return render(request, 'pannah/homepage.html', context)

@login_required(login_url='login')
def schemes(request):
	schemes = Scheme.objects.all()
	total_schemes = schemes.count()

	context = {'schemes':schemes, 'total_schemes':total_schemes}
	return render(request, 'pannah/schemes.html', context)

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('name')
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
		

	context = {'form':form}
	#return HttpResponse("Register")
	return render(request, 'pannah/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'pannah/login.html', context)

def resetPassword(request):
	return HttpResponse('Reset')

def membership(request):
	context={}
	return render(request, 'pannah/membership.html')



# Create your views here.
