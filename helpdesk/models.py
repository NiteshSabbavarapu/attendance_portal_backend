from enum import Enum

from django.db import models


class Gender(Enum):
    Male = "M"
    Female = "F"

    @classmethod
    def choice(cls):
        gender_list = []
        for i in cls:
            gender_list.append((i.name, i.value))
        return gender_list


class Role(Enum):
    Mentor = "M"
    Student = "S"

    @classmethod
    def choice(cls):
        role_list = []
        for i in cls:
            role_list.append((i.name, i.value))
        return role_list


class Status(Enum):
    Present = "present"
    Absent = "absent"

    @classmethod
    def choice(cls):
        status_list = []
        for i in cls:
            status_list.append((i.name, i.value))
        return status_list


class UserAccount(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=Gender.choice())
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self):
        return f"User is {self.name}"


class UserRole(models.Model):
    user_account = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=Role.choice())


class AttendanceDetails(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    Date = models.DateField()
    punch_in_time = models.DateTimeField(auto_now=True)
    punch_out_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choice())

