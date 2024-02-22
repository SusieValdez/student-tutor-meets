from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard', views.home),
    path('meetings/', views.meetings),
    path('students/', views.students),
    path('calendar/', views.calendar),
    path('notes/', views.notes),

]
