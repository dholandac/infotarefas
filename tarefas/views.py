from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    completed_tasks = len(tasks)
    total_tasks = 0
    remaining_tasks = 0
    pct = 0

    return render(
        request, 
        'tarefas/home.html',
        {
            'tasks' : tasks,
            'total' : total_tasks,
            'completed' : completed_tasks,
            'remaining' : remaining_tasks,
            'pct' : pct
        })

def add(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        
    return redirect('home')