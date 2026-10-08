from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.

def hello(request):
    data = {
        'name' : "rahul",
        'tasks' : [
            "Learn Django",
            "Practice Python",
            "Complete homework",
            "Read a book"
    ]}
    return render(request, "tasks/hello.html", {'data':data})

def about(request):
    stu_data = {
        'name': "Rahul",
        'school': "ABC Public School"
    }
    
    return render(request, "tasks/about.html", {'stu_data':stu_data})


def task_list(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

    else:

        form = TaskForm()

    tasks = Task.objects.all()

    return render(
        request,
        'tasks/task_list.html',
        {
            'tasks': tasks,
            'form': form
        }
    )


def task_edit(request, id):
    task = Task.objects.get(id = id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance= task)

        if form.is_valid():
            form.save()
    else:
        form = TaskForm(instance= task)

    return render(request,
                  "tasks/task_edit.html",
                  {
                      'form':form,
                      'task': task
                  })


def task_delete(request, id):
    task = Task.objects.get(id=id)

    if request.method == "POST":
        task.delete()

    return  redirect('/tasks/')