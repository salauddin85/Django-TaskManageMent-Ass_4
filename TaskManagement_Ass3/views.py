from django.shortcuts import render,redirect

from Task.models import Task


def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def home(request):
    return render(request,'base.html')