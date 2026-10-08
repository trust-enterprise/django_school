"""
URL configuration for school_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from tasks.views import hello, about, task_list, task_edit, task_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('about/', about),
    path('tasks/', task_list),
    path('tasks/edit/<int:id>/', task_edit),
    path('tasks/delete/<int:id>/', task_delete)
]
