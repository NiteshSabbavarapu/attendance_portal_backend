from datetime import datetime
from attendance_tracker.models.models import Attendance_punch_in_model
from attendance_tracker.interactors.Storage_interfaces.PunchInStorageInterface import \
    PunchInInterface


class PunchInStorageImplementation(PunchInInterface):
    def create_punch_in(self, user_id: int):
        current_time = datetime.now()
        morning_10 = current_time.replace(hour=10, minute=0, second=0)
        punch_in_instance_of_day = Attendance_punch_in_model.objects.filter(
            user_id=user_id,
            punch_in__date=current_time.date()
        )

        if punch_in_instance_of_day.exists():
            return "you have already punched in as {}".format(
                punch_in_instance_of_day[0].attendance_status)

        if current_time.weekday() == 6:
            Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Holiday"
            )
            return None

        if current_time > morning_10:
            Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Absent"
            )
            return "Absent"
        else:
            punch_in_instance = Attendance_punch_in_model.objects.create(
                user_id=user_id, attendance_status="Present"
            )
            return punch_in_instance

    def mark_absent_for_no_punch_in(self, user_id: int):
        current_time = datetime.now()

        if current_time.weekday() == 6:
            return

        morning_10 = current_time.replace(hour=10, minute=0, second=0)

        if not Attendance_punch_in_model.objects.filter(
                user_id=user_id,
                punch_in__date=current_time.date()
        ).exists():
            Attendance_punch_in_model.objects.create(
                user_id=user_id,
                attendance_status="Absent",
                punch_in=morning_10
            )
