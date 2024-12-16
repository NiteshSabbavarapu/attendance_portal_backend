from abc import ABC, abstractmethod


class AttendanceFilterStorageInterface(ABC):
    @abstractmethod
    def get_filtered_attendance(self, user_id, status, start_date,
                                end_date):
        pass
