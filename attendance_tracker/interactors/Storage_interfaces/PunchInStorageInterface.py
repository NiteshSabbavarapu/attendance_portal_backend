from abc import ABC, abstractmethod


class PunchInInterface(ABC):
    @abstractmethod
    def create_punch_in(self, user: int):
        pass
