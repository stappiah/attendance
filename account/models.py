# In your app's models.py file
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# USER_TYPES = [
#     ("lecturer", "Lecturer"),
#     ("student", "Student"),
# ]

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


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email address is required")
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    # user_type = models.CharField(max_length=8, choices=USER_TYPES, default="student")
    # program = models.CharField(max_length=27, choices=PROGRAMS, blank=True, null=True)
    # index_number = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
