from abc import ABC, abstractmethod


class PunchOutPresenterInterface(ABC):
    @abstractmethod
    def punch_out_attendance_response(self, storage):
        pass
