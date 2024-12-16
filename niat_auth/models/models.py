from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    student_id = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role
