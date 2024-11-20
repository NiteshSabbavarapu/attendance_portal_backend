from attendance_tracker.storage.AttendaceReportStorageImplementation import \
    AttendanceReportStorageImplementation
from attendance_tracker.presenters.AttendaceReportPresenterImplementation import (
    AttendanceReportPresenterImplementation)


class AttendanceReportInteractor:
    def __init__(self, storage: AttendanceReportStorageImplementation,
                 presenter: AttendanceReportPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def get_recent_attendance_history(self, user_id: int, date: str):
        attendance_history = self.storage.get_user_attendance(user_id, date)
        return self.presenter.attendance_report_response(attendance_history)
