from datetime import datetime
from attendance_tracker.models.models import Attendance_punch_in_model
from attendance_tracker.interactors.Storage_interfaces.AttendanceFilterStorageInterface import \
    AttendanceFilterStorageInterface


class AttendanceFilterStorageImplementation(AttendanceFilterStorageInterface):
    def get_filtered_attendance(self, user_id, status=None, start_date=None,
                                end_date=None):
        records = Attendance_punch_in_model.objects.filter(user_id=user_id)

        if status:
            records = records.filter(attendance_status=status)
        if start_date:
            records = records.filter(
                punch_in__date__gte=datetime.strptime(start_date,
                                                      "%Y-%m-%d").date())
        if end_date:
            records = records.filter(
                punch_in__date__lte=datetime.strptime(end_date,
                                                      "%Y-%m-%d").date())

        return records
