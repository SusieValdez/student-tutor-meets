from django.shortcuts import render
from django.db.models import Q
from .models import Student


def home(request):
    return render(request, "main/dashboard.html")


def meetings(request):
    return render(request, "main/meetings.html")


def students(request):
    if request.method == "POST":
        query = request.POST["query"]
        # Filter students by name, email, or ID
        students = Student.objects.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(student_id__icontains=query)
        )
        return render(request, "main/students.html", {"students": students})

    # Fetch all students
    students = Student.objects.all()
    return render(request, "main/students.html", {"students": students})


def notes(request):
    return render(request, "main/notes.html")


def calendar(request):
    return render(request, "main/calendar.html")
