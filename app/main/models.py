from django.db import models


class BaseUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic_url = models.CharField(
        max_length=2000, default="main/img/default_profile_pic.jpg"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Tutor(BaseUser):
    pass


class Student(BaseUser):
    personal_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    course = models.CharField(max_length=200)
