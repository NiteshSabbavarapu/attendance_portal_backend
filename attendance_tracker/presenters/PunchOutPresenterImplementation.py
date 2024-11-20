from django.http import JsonResponse
from rest_framework import status
from attendance_tracker.interactors.presenter_interfaces.PunchoutPresenterInterface import (
    PunchOutPresenterInterface)


class PunchOutPresenterImplementation(PunchOutPresenterInterface):
    def punch_out_attendance_response(self, punch_out_instance):
        response_data = {
            "message": f"Attendance punched out successfully at {punch_out_instance.punch_out}",
            "note": punch_out_instance.note_of_the_day,
            "status_code": status.HTTP_200_OK
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
