from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("home/", views.home, name='home'),
    path("students/", views.students, name="students"),
    path('superuser/', views.superuser, name='superuser'),
    path('manage_student/', views.manage_student, name='manage_student'),
    path('manage_tutor/', views.manage_tutor, name='manage_tutor'),
    path('tutor/', views.tutor, name='tutor'),
]