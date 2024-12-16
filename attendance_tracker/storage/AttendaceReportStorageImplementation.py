from datetime import datetime
from attendance_tracker.models import *
from attendance_tracker.interactors.Storage_interfaces.AttendanceReportStorageInterface import \
    (AttendanceReportStorageInterface)


class AttendanceReportStorageImplementation(AttendanceReportStorageInterface):
    def get_recent_user_attendance(self, user_id: int):
        # Fetch the 5 most recent punch-ins and punch-outs for the user
        recent_punch_ins = (
            Attendance_punch_in_model.objects.filter(user_id=user_id)
            .select_related('user')
            .order_by('-punch_in')[:5]  # Adjust the number of records as needed
        )

        recent_punch_outs = (
            Attendance_punch_out_model.objects.filter(user_id=user_id)
            .order_by('-punch_out')[:5]
        )

        attendance_history = []
        for punch_in, punch_out in zip(recent_punch_ins, recent_punch_outs):
            attendance_history.append({
                "user_id": user_id,
                "punch_in": punch_in.punch_in,
                "punch_out": punch_out.punch_out if punch_out else None,
                "note_of_the_day": punch_out.note_of_the_day if punch_out else None,
            })

        return attendance_history
