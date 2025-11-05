from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    tasks = Task.objects.all()
    completed_tasks = 0
    total_tasks = len(tasks)
    remaining_tasks = 0
    pct = 0

    for task in tasks:
        if task.done == True:
            completed_tasks += 1

    remaining_tasks = total_tasks - completed_tasks

    if total_tasks > 0:
        pct = int((completed_tasks / total_tasks) * 100)

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

def toggle(request, id):
    task = get_object_or_404(Task, id=id)

    if task.done == True:
        task.done = False
    else:
        task.done = True

    task.save()

    return redirect('home')

def delete(request, id):
    task = get_object_or_404(Task, id=id)

    task.delete()
    return redirect('home')