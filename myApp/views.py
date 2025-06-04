from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi, I am Harsh Jain. This is my first Django app")

# Create your views here.
