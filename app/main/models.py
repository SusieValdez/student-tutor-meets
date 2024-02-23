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
    def __repr__(self):
        return f"<Tutor: {self.name}>"


class Student(BaseUser):
    personal_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Student: {self.name}>"
