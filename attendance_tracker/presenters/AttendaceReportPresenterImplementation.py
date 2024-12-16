from django.http import JsonResponse
from rest_framework import status

from attendance_tracker.interactors.presenter_interfaces.AttendanceReportPresenterInterface import \
    AttendanceReportPresenterInterface


class AttendanceReportPresenterImplementation(
    AttendanceReportPresenterInterface):
    def attendance_report_response(self, attendance_history):
        response_data = {
            "recent_attendance_history": attendance_history,
            "status_code": status.HTTP_200_OK
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)
