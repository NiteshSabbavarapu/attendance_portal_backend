from abc import ABC, abstractmethod


class AttendanceInfoStorageInterface(ABC):
    def get_user_attendance(self, user, date):
        pass
