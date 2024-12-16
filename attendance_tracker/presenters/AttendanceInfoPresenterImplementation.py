from django.http import JsonResponse
from rest_framework import status
from attendance_tracker.interactors.presenter_interfaces.AttendanceInfoPresenterInterface import \
    AttendanceInfoPresenterInterface


class AttendanceInfoPresenterImplementation(AttendanceInfoPresenterInterface):
    def user_attendance_percentage(self, attendance_data):
        response_data = {
            "user_attendance_percentage": attendance_data[
                'attendance_percentage'],
            "present_days": attendance_data['present_days'],
            "absent_days": attendance_data['absent_days'],
            "remaining_days": attendance_data['remaining_days'],
            "status_code": status.HTTP_200_OK
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
