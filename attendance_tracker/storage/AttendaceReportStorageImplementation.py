from datetime import datetime
from attendance_tracker.models import *
from attendance_tracker.interactors.Storage_interfaces.AttendanceReportStorageInterface import \
    (AttendanceReportStorageInterface)


class AttendanceReportStorageImplementation(AttendanceReportStorageInterface):
    def get_user_attendance(self, user_id: int, date: str):
        input_date = datetime.strptime(date, '%Y-%m-%d')
        year = input_date.year
        month = input_date.month

        attendance_records = (
            Attendance_punch_in_model.objects.filter(
                user_id=user_id,
                punch_in__year=year,
                punch_in__month=month
            )
            .select_related('user')
            .order_by('-punch_in')
        )

        punch_out_records = Attendance_punch_out_model.objects.filter(
            user_id=user_id,
            punch_out__year=year,
            punch_out__month=month
        ).order_by('-punch_out')

        attendance_history = []
        for punch_in, punch_out in zip(attendance_records, punch_out_records):
            attendance_history.append({
                "user_id": user_id,
                "punch_in": punch_in.punch_in,
                "punch_out": punch_out.punch_out if punch_out else None,
                "note_of_the_day": punch_out.note_of_the_day if punch_out else None,
            })

        return attendance_history
