from abc import ABC, abstractmethod


class PunchInPresenterInterface(ABC):
    @abstractmethod
    def punch_in_attendance_response(self, storage):
        pass
