from django.db import models


class Attendance_punch_in_model(models.Model):
    user = models.ForeignKey('niat_auth.User', on_delete=models.CASCADE)
    punch_in = models.DateTimeField(auto_now_add=True)
    attendance_status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)


class Attendance_punch_out_model(models.Model):
    user = models.ForeignKey('niat_auth.User', on_delete=models.CASCADE)
    punch_out = models.DateTimeField(auto_now_add=True)
    note_of_the_day = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)
