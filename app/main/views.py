from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .decorators import allowed_users, admin_only
from .models import Student, Tutor
from .forms import CreateUserForm


@login_required
@admin_only
def home(request):
    return render(request, "main/pages/home.html", {"user": request.user})


@login_required
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


@login_required
@allowed_users(allowed_roles=['admin'])
def superuser(request):
    return render(request, 'admin/superuser.html')


@allowed_users(allowed_roles=['admin'])
def manage_student(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'admin/student/manage_student.html', {'form': form})


@allowed_users(allowed_roles=['admin'])
def manage_tutor(request):
    # Filter search results for tutors
    if request.method == "POST":
        query = request.POST["query"]
        # Filter students by name, email, or ID
        tutor = Tutor.objects.filter(
            Q(name__icontains=query)
            | Q(email__icontains=query)
        )
    # Create new tutors
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'admin/student/manage_tutor.html', {'form': form})


def tutor(request):
    return render(request, 'main/pages/tutor.html')
