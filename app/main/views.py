from django.shortcuts import render
from django.db.models import Q
from .models import Student


def home(request):
    return render(request, "main/pages/home.html", {"user": request.user})


def students(request):
    if request.method == "POST":
        query = request.POST["query"]
        # Filter students by name, email, or ID
        students = Student.objects.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
            | Q(student_id__icontains=query)
        )
        return render(request, "main/pages/students.html", {"students": students})

    # Fetch all students
    students = Student.objects.all()
    return render(request, "main/pages/students.html", {"students": students})
