from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def homepage(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect("homepage")
        else:
            form = TaskForm()

    all_tasks = Task.objects.all()
    paginator = Paginator(all_tasks, 5)
    page = request.GET.get('page')
    all_tasks = paginator.get_page(page)

    context = {
        'all_tasks': all_tasks,
    }
    return render(request, "todolist/index.html", context)

def profilepage(request):
    return render(request, "todolist/profile.html")

def todo_details_page(request, todo_id):
    task = Task.objects.get(id=todo_id)
    return render(request, "todolist/todo_details.html", {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if task:
        task.delete()
        messages.success(request, f"Task - {task.task} deleted!")
        page = request.GET.get('page', '1')
        return redirect(f"/?page={page}")
    messages.error(request, "Task not found to delete")

def edit_task(request, task_id):
    task = Task.objects.get(id = task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.save()
            messages.success(request, "Task added successfully!")
            return redirect("homepage")
    print("Task from edit view:", task)
    return render(request, "todolist/edit_task.html", {'task': task})

def mark_incomplete(request, task_id):
    task = Task.objects.get(id = task_id)
    task.isCompleted = False
    messages.success(request, "Task marked incomplete!")
    task.save()
    page = request.GET.get('page', '1')
    return redirect(f"/?page={page}")

def mark_complete(request, task_id):
    task = Task.objects.get(id = task_id)
    task.isCompleted = True
    messages.success(request, "Task marked complete!")
    task.save()
    page = request.GET.get('page', '1')
    return redirect(f"/?page={page}")