from rest_framework import serializers
from attendance_tracker.models.models import *


class AttendancePunchInSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_punch_in_model
        fields = ['id', 'user', 'punch_in', 'attendance_status']


class AttendancePunchOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance_punch_out_model
        fields = ['id', 'user', 'punch_out', 'note_of_the_day']


class AttendanceInfoSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    date = serializers.DateField()
