from abc import ABC, abstractmethod


class AttendanceInfoPresenterInterface(ABC):
    @abstractmethod
    def user_attendance_percentage(self, interactor):
        pass
