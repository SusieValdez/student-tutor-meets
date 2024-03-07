from django.shortcuts import render
from .models import Tutor, Student


def home(request):
    return render(request, "main/dashboard.html")


def meetings(request):
    return render(request, "main/meetings.html")


def students(request):
    display_student = Student.objects.all()
    return render(request, "main/students.html", {"students": display_student})
    if request.method == 'POST':
        search_query= request.POST('search_query')
        posts= Student.objects.filter(name__contains=search_query)
        return render(request, "main/students.html", {'query':search_query, 'search':posts})
    else:
        return render(request, 'main/students.html', {})

def notes(request):
    return render(request, "main/notes.html")


def calendar(request):
    return render(request, "main/calendar.html")
