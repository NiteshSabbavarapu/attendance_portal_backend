from abc import ABC, abstractmethod


class AttendanceReportStorageInterface(ABC):
    @abstractmethod
    def get_recent_user_attendance(self, user_id: int):
        pass
