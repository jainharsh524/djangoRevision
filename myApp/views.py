from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi, I am Harsh Jain. This is my first Django app")

def test(request, id, name):
    return HttpResponse(f"Hi, I am {name} and my I'd is {id}")

def batch(request, className):
    return HttpResponse(f"I am in Batch {className}")

def department(request, deptName):
    return HttpResponse(f"I am in {deptName} department")

# Create your views here.
