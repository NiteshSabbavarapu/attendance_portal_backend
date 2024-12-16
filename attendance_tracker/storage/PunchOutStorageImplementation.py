from datetime import datetime

from attendance_tracker.models import Attendance_punch_in_model
from attendance_tracker.models.models import Attendance_punch_out_model
from attendance_tracker.interactors.Storage_interfaces.PunchOutStorageInterface import \
    PunchOutStorageInterface


class PunchOutStorageImplementation(PunchOutStorageInterface):
    def create_punch_out(self, user_id: int, note: str):
        current_time = datetime.now()
        if not Attendance_punch_in_model.objects.filter(
                user_id=user_id,
                attendance_status="Present"
        ).exists():
            return None

        if Attendance_punch_out_model.objects.filter(
                user_id=user_id,
                punch_out__date=current_time.date()
        ).exists():
            return "you have already punched out"
        punch_out_instance = Attendance_punch_out_model.objects.create(
            user_id=user_id, note_of_the_day=note)
        return punch_out_instance
