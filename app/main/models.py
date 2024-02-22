from django.db import models


class Tutor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __repr__(self):
        return f"<Tutor: {self.name}>"


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    personal_tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    def __repr__(self):
        return f"<Student: {self.name}>"
