from . import views
from django.urls import path

urlpatterns = [
    path("",views.student_api.as_view(),name="student_api"),
]
