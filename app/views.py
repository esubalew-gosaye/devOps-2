from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
	return HttpResponse("<h1>Welcome to CI/CD</h1>")

def index(request):
	return HttpResponse("<body><h1>INDEX PAGE</h1><h2>INDEX PAGE</h2><body>")