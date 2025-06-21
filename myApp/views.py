from django.shortcuts import render
from django.http import HttpResponse
from .models import Student_Profile

def home(request):
    context = {'lang':'Django',
               'list':['Books', 'Pens', 'Vegies'],
               'user_logged_in': True,
               'username': 'Harsh'
               }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def users(request):
    profiles = Student_Profile.objects.all() 
    # A way to get collection of all the objects of a class
    context = {'profiles': profiles} 
    # after that wrap it into a dict
    return render(request, 'users.html', context)

def test(request, id, name):
    return HttpResponse(f"Hi, I am {name} and my I'd is {id}")

def batch(request, className):
    return HttpResponse(f"I am in Batch {className}")

def department(request, deptName):
    return HttpResponse(f"I am in {deptName} department")

# Create your views here.
