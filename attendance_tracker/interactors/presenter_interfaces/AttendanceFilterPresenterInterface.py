from abc import ABC, abstractmethod


class AttendanceFilterPresenterInterface(ABC):
    @abstractmethod
    def present_filtered_attendance(self, attendance_data):
        pass
