from datetime import datetime
from attendance_tracker.models.models import Attendance_punch_in_model
from attendance_tracker.interactors.Storage_interfaces.PunchInStorageInterface import \
    PunchInInterface


class PunchInStorageImplementation(PunchInInterface):
    def create_punch_in(self, user_id: int):
        current_time = datetime.now()
        morning_10 = current_time.replace(hour=10, minute=0, second=0)

        # Check if today is a weekend (Sunday = 6, Saturday = 5)
        if current_time.weekday() == 6:  # Sunday
            Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Holiday"
            )
            return None

        # If punch-in occurs after 10:00 AM
        if current_time > morning_10:
            Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Absent"
            )
            return None
        else:
            punch_in_instance = Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Present"
            )
            return punch_in_instance

    def mark_absent_for_no_punch_in(self, user_id: int):
        current_time = datetime.now()
        # Check if today is a weekend
        if current_time.weekday() == 6:  # Sunday
            return  # Do nothing, it's a holiday

        morning_10 = current_time.replace(hour=10, minute=0, second=0)
        # Record absence if no punch-in occurred by 10:00 AM
        if not Attendance_punch_in_model.objects.filter(
                user_id=user_id,
                punch_in__date=current_time.date()
        ).exists():
            Attendance_punch_in_model.objects.create(
                user_id=user_id,
                attendance_status="Absent",
                punch_in=morning_10
            )
