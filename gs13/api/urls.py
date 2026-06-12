from . import views
from django.urls import path

urlpatterns = [
    # path("",views.StudentList.as_view(),name="StudentList"),
    # path("",views.StudentCreate.as_view(),name="StudentCreate"),
    # path("",views.StudentRetrieve.as_view(),name="StudentRetrieve"),
    # path("",views.StudentUpdate.as_view(),name="StudentUpdate"),
    path("",views.StudentDestroy.as_view(),name="StudentDestroy"),
]
