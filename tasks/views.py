from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Task, TaskGroup
from .forms import TaskGroupForm, TaskForm

def index(request):
    return render(request, 'tasks/index.html', {'now':datetime.now()})

@login_required
def dashboard(request):
    groups = TaskGroup.objects.filter(user=request.user).prefetch_related("tasks")

    group_form = TaskGroupForm()
    task_form = TaskForm()

    if request.method == "POST":
        if "create_group" in request.POST:
            group_form = TaskGroupForm(request.POST)
            if group_form.is_valid():
                new_group = group_form.save(commit=False)
                new_group.user = request.user
                new_group.save()
                return redirect("dashboard")
            
        elif "create_task" in request.POST:
            task_form = TaskForm(request.POST)
            if task_form.is_valid():
                new_task = task_form.save(commit=False)
                new_task.user = request.user
                new_task.save()
                return redirect("dashboard")
            
    return render(
        request,
        "tasks/dashboard.html",
        {
            "groups":groups,
            "group_form":group_form,
            "task_form":task_form,
        },
    )