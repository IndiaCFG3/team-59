from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return HttpResponse("Home page")

def schemes(request):
	return HttpResponse("Scheme Page")

# Create your views here.
