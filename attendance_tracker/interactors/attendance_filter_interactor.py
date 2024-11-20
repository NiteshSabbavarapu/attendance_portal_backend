from attendance_tracker.presenters.AttendanceFilterPresenterImplementation import \
    AttendanceFilterPresenterImplementation
from attendance_tracker.storage.AttendanceFilterStorageImplementation import \
    AttendanceFilterStorageImplementation


class AttendanceFilterInteractor:
    def __init__(self, storage: AttendanceFilterStorageImplementation,
                 presenter: AttendanceFilterPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def filter_attendance(self, user_id, status=None, start_date=None,
                          end_date=None):
        attendance_records = self.storage.get_filtered_attendance(
            user_id=user_id, status=status, start_date=start_date,
            end_date=end_date)
        return self.presenter.present_filtered_attendance(attendance_records)
