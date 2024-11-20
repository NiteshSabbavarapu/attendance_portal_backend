from abc import ABC, abstractmethod


class PunchInInterface(ABC):
    @abstractmethod
    def create_punch_in(self, user: int):
        pass

    @abstractmethod
    def mark_absent_for_no_punch_in(self, user: int):
        pass
