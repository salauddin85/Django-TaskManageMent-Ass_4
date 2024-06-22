from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def add_task(request):
    task_form = TaskForm()
    if request.method=='POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('taskpage')
        else:
            task_form = TaskForm()
    return render(request,'task.html',{'form':task_form})

def edit_task(request,id):
    task = Task.objects.get(pk = id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('show_tasks')
   
    return render(request, 'edit_task.html', {'form': form})

def delete_task(request,id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('show_tasks')
 
