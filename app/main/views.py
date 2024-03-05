from django.shortcuts import render
from .models import Tutor, Student


fake_tutor = Tutor(name="Minerva McGonagall", email="xX-kitten-witch-Xx@gmail.com")
fake_students = [
    Student(
        name="Harry Potter",
        email="the_chosen_one@hotmail.co.uk",
        profile_pic_url="https://www.looper.com/img/gallery/why-harry-potters-scar-is-more-disturbing-than-you-think/intro-1603724418.jpg",
        personal_tutor=fake_tutor,
    ),
    Student(
        name="Ron Weasley",
        email="scabbers_king@aol.co.uk",
        profile_pic_url="https://media.hollywood.com/images/638x425/1935663.jpg",
        personal_tutor=fake_tutor,
    ),
    Student(
        name="Hermione Granger",
        email="its_leviosaaaa@gmail.com",
        profile_pic_url="https://static.wikia.nocookie.net/harrypotter/images/7/78/Wingardium_Leviosa_2.jpg/revision/latest/scale-to-width-down/396?cb=20110713200101&path-prefix=fr",
        personal_tutor=fake_tutor,
    ),
]


def home(request):
    return render(request, "main/pages/home.html", {"user": request.user})


def students(request):
    return render(request, "main/pages/students.html", {"students": fake_students})
