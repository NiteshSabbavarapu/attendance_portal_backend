from django.http import JsonResponse
from rest_framework import status
from attendance_tracker.interactors.presenter_interfaces.PunchInPresenterInterface import (
    PunchInPresenterInterface)


class PunchInPresenterImplementation(PunchInPresenterInterface):
    def punch_in_attendance_response(self, punch_in_instance):
        response_data = {
            "message": f"Attendance punched in successfully at {punch_in_instance.punch_in}",
            "status_code": status.HTTP_200_OK
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
