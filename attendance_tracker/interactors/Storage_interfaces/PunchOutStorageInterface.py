from abc import ABC, abstractmethod


class PunchOutStorageInterface(ABC):
    @abstractmethod
    def create_punch_out(self, user: int, note_of_the_day: str):
        pass
