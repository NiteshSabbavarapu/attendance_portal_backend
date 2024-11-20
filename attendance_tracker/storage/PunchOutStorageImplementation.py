from attendance_tracker.models.models import Attendance_punch_out_model
from attendance_tracker.interactors.Storage_interfaces.PunchOutStorageInterface import \
    PunchOutStorageInterface


class PunchOutStorageImplementation(PunchOutStorageInterface):
    def create_punch_out(self, user_id: int, note: str):
        punch_out_instance = Attendance_punch_out_model.objects.create(
            user_id=user_id, note_of_the_day=note)
        return punch_out_instance
