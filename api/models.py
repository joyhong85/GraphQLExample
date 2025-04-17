from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=20)
    grade = models.IntegerField()


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    classroom = models.CharField(max_length=10)


class Professor(models.Model):
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

