from django.db import models
from django.conf import settings
from account.models import Account


PROGRAMS = [
    ("Information Technology", "Information Technology"),
    ("Purchasing and Supply", "Purchasing and Supply"),
    ("Accountancy", "Accountancy"),
    ("Computer Network Management", "Computer Network Management"),
    ("Computer Science", "Computer Science"),
    ("Automotive Engineering", "Automotive Engineering"),
    ("Building Technology", "Building Technology"),
    ("Civil Engineering", "Civil Engineering"),
]

programType = [
    ("Higher National Diploma (HND)", "Higher National Diploma (HND)"),
    ("Bachelor of Technology (BTECH)", "Bachelor of Technology (BTECH)"),
    ("BTECH (Top Up)", "BTECH (Top Up)"),
    ("Certificate", "Certificate"),
    ("Diploma", "Diploma"),
]


# Create your models here.
class Course(models.Model):
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=10)
    course_name = models.CharField(max_length=100)


class Session(models.Model):
    lecturer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    program = models.CharField(max_length=27, choices=PROGRAMS)
    created = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.CharField(max_length=10)
    program_type = models.CharField(max_length=30, choices=programType)
    status = models.BooleanField(default=True)

    def session_course(self):
        return self.course.course_name

    class Meta:
        ordering = ["-created"]


class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_student(self):
        return f"{self.student.first_name} {self.student.last_name}"

    def get_program(self):
        return self.session.program

    def get_index_number(self):
        return self.student.index_number

    class Meta:
        ordering = ["-id"]
