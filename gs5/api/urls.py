from django.urls import path
from . import views

urlpatterns = [
    path("student_api/",views. student_api.as_view(),name="student_api"),

]