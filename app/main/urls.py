from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home/", views.home, name="home"),
    path("students/", views.students, name="students"),
    path("meetings/", views.meetings, name="meetings"),
    path("meetings/list", views.meetings_list, name="meetings_list"),
]
