from . import views
from django.urls import path

urlpatterns = [
    path("",views.student_api,name="student_api"),
]
