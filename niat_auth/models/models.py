import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta


class AuthToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255, unique=True)
    refresh_token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    def has_expired(self):
        return timezone.now() > self.expires_at

    @staticmethod
    def generate_token():
        return uuid.uuid4().hex

    @staticmethod
    def get_expiry():
        return timezone.now() + timedelta(days=30)

    def __str__(self):
        return str(self.user)


# class UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     role = models.CharField(max_length=255)
#     gender = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f"{self.user} - {self.role}"
