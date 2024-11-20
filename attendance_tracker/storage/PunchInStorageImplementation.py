from datetime import datetime

from attendance_tracker.models.models import Attendance_punch_in_model
from attendance_tracker.interactors.Storage_interfaces.PunchInStorageInterface import \
    PunchInInterface


class PunchInStorageImplementation(PunchInInterface):
    def create_punch_in(self, user_id: int):
        current_time = datetime.now()
        morning_10 = current_time.replace(hour=10, minute=0, second=0)

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
