from . import views
from django.urls import path,include

urlpatterns = [
    path("",views.Student_create,name='Student_create'),
]