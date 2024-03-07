from django.db import models


class BaseUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic_url = models.CharField(
        max_length=2000, default="img/default_profile_pic.jpg"
    )

    class Meta:
        abstract = True


class Tutor(BaseUser):
    def __str__(self):
        return (self.name)


class Student(BaseUser):
    personal_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student_id = models.IntegerField()
    course = models.CharField(max_length=200),


    def __str__(self):
        return (self.name)
