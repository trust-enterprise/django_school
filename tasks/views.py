from django.shortcuts import render
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

            title = form.cleaned_data["title"]

            Task.objects.create(
                title=title
            )

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