from django.shortcuts import render
from django.http import HttpResponse
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
    
