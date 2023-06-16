from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title' : 'Homepage', 'tasks' : tasks})

def about(request):
    return render(request, 'main/about.html')

def show_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    
    context = {
        'task': task
    }
    return render(request, 'main/task-detail.html', context)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Form is not valid'

    form = TaskForm()

    context = {
        'form' : form,
        'error' : error
    }
    return render(request, 'main/create.html', context)

def update(request, pk):
    task = get_object_or_404(Task,id=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if task.is_complete == False:
                form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)

    context = {
        'form' : form,
        'task' : task
    }
    
    return render(request, 'main/create.html', context)

def delete(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('home')

