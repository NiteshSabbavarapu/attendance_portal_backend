from django.http import JsonResponse
from rest_framework import status
from attendance_tracker.interactors.presenter_interfaces.AttendanceFilterPresenterInterface import \
    AttendanceFilterPresenterInterface


class AttendanceFilterPresenterImplementation(AttendanceFilterPresenterInterface):
    def present_filtered_attendance(self, attendance_records):
        data = [
            {
                "date": record.punch_in.date(),
                "status": record.attendance_status,
                "time": record.punch_in.time(),
            }
            for record in attendance_records
        ]
        return JsonResponse({"attendance_records": data},
                            status=status.HTTP_200_OK)
