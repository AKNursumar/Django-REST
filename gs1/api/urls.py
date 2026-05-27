from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("stuinfo/<int:pk>",views.student_detail,name="student_detail"),
    path("stulist",views.student_list,name="student_list"),
]