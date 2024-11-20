from abc import ABC, abstractmethod


class AttendanceReportPresenterInterface(ABC):
    @abstractmethod
    def attendance_report_response(self, storage):
        pass
