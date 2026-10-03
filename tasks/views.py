from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    return HttpResponse("hello django")

def about(request):
    return HttpResponse("This is our School Task Manager.")
