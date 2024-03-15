from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Student, Meeting
from datetime import date, time
from .models import Meeting

fake_meeting_data = [
    Meeting(
        date=date.fromisoformat("2021-03-01"),
        start_time=time.fromisoformat("09:00"),
        end_time=time.fromisoformat("10:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-01"),
        start_time=time.fromisoformat("10:00"),
        end_time=time.fromisoformat("11:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-01"),
        start_time=time.fromisoformat("11:00"),
        end_time=time.fromisoformat("12:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-02"),
        start_time=time.fromisoformat("09:00"),
        end_time=time.fromisoformat("10:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-02"),
        start_time=time.fromisoformat("11:00"),
        end_time=time.fromisoformat("12:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-10"),
        start_time=time.fromisoformat("09:00"),
        end_time=time.fromisoformat("10:00"),
    ),
    Meeting(
        date=date.fromisoformat("2021-03-10"),
        start_time=time.fromisoformat("10:00"),
        end_time=time.fromisoformat("11:00"),
    ),
]


@login_required
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
def meetings(request):
    # Calculate days in months and day of week month starts on
    # TODO: Replace with real data
    num_days_in_month = 31
    day_of_week_month_starts_on = 5  # Friday
    num_days_in_previous_month = 29

    meetings = fake_meeting_data  # TODO: Replace with real data from database

    # Days from previous month
    padding_start_day = (
        num_days_in_previous_month - (day_of_week_month_starts_on - 1) + 1
    )
    padding_start_days = [
        {
            "date": date,
            "meetings": [],
            "is_in_current_month": False,
        }
        for date in range(padding_start_day, num_days_in_previous_month + 1)
    ]

    # Days from current month
    meeting_days = [
        {
            "date": date,
            "meetings": [meeting for meeting in meetings if meeting.date.day == date],
            "is_in_current_month": True,
        }
        for date in range(1, num_days_in_month + 1)
    ]

    # Days from next month
    padding_end_day = (7 - (len(meeting_days) + len(padding_start_days))) % 7
    padding_end_days = [
        {
            "date": date,
            "meetings": [],
            "is_in_current_month": False,
        }
        for date in range(1, padding_end_day + 1)
    ]

    # Combine all days
    days = padding_start_days + meeting_days + padding_end_days

    return render(
        request,
        "main/pages/meetings.html",
        {
            "user": request.user,
            "days": days,
        },
    )


@login_required
def meetings_list(request):
    return render(
        request,
        "main/pages/meetings_list.html",
        {
            "user": request.user,
            "meetings": fake_meeting_data,
        },
    )
