"""
URL configuration for gs15 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("student_api/",views.StudentList.as_view()),
    # path("student_api/",views.StudentCreate.as_view()),
    # path("student_api/<int:pk>",views.StudentRetrieve.as_view()),
    # path("student_api/<int:pk>",views.StudentUpdate.as_view()),
    # path("student_api/<int:pk>",views.StudentDestroy.as_view()),
    # path("student_api/",views.StudentListCreate.as_view()),
    # path("student_api/<int:pk>",views.StudentRetrieveUpdate.as_view()),
    # path("student_api/<int:pk>",views.StudentRetrieveDestroy.as_view()),
    path("student_api/<int:pk>",views.StudentRetrieveUpdateDestroy.as_view()),
]
