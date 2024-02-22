from django.shortcuts import render


def home(request):
    return render(request, "main/dashboard.html")


def meetings(request):
    return render(request, "main/meetings.html")


def students(request):
    return render(request, "main/students.html")


def notes(request):
    return render(request, "main/notes.html")


def calendar(request):
    return render(request, "main/calendar.html")
