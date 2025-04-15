from django.db import models
from django.conf import settings

PROGRAMS_TYPE = [
    ("hnd", "Higher National Diploma"),
    ("diploma", "Diploma"),
    ("btech", "B-Tech"),
]

PROGRAMS = [
    ("computer science", "Computer Science"),
    ("information technology", "Information Technology"),
    ("purchasing and supply", "Purchasing and Supply"),
]


# Create your models here.
class Student(models.Model):
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    index_number = models.CharField(max_length=20)
    program_type = models.CharField(max_length=7, choices=PROGRAMS_TYPE)
    program = models.CharField(max_length=22, choices=PROGRAMS)
    fingerprint = models.BinaryField()


class Course(models.Model):
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)
