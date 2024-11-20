import calendar
from datetime import datetime
from attendance_tracker.models import Attendance_punch_in_model
from attendance_tracker.interactors.Storage_interfaces.AttendanceInfoStorageInterface import \
    AttendanceInfoStorageInterface


class AttendanceInfoStorageImplementation(AttendanceInfoStorageInterface):

    def get_user_attendance(self, user_id: int, date: str):
        input_date = datetime.strptime(date, '%Y-%m-%d')
        year = input_date.year
        month = input_date.month

        user_attendance = Attendance_punch_in_model.objects.filter(
            user_id=user_id,
            punch_in__year=year,
            punch_in__month=month,
            attendance_status="Present"
        ).values('punch_in__date').distinct()

        user_absent = Attendance_punch_in_model.objects.filter(
            user_id=user_id,
            punch_in__year=year,
            punch_in__month=month,
            attendance_status="Absent"
        ).values('punch_in__date').distinct()

        total_days_in_month = calendar.monthrange(year, month)[1]
        present_days = len(user_attendance)
        absent_days = len(user_absent)
        remaining_days = total_days_in_month - present_days - absent_days
        attendance_percentage = (
                                        present_days / total_days_in_month) * 100 if total_days_in_month else 0

        return {
            "attendance_percentage": attendance_percentage,
            "present_days": present_days,
            "absent_days": absent_days,
            # "remaining_days": remaining_days
        }
