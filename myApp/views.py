from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {'lang':'Django',
               'list':['Books', 'Pens', 'Vegies'],
               'user_logged_in': True,
               'username': 'Harsh'
               }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def test(request, id, name):
    return HttpResponse(f"Hi, I am {name} and my I'd is {id}")

def batch(request, className):
    return HttpResponse(f"I am in Batch {className}")

def department(request, deptName):
    return HttpResponse(f"I am in {deptName} department")

# Create your views here.
