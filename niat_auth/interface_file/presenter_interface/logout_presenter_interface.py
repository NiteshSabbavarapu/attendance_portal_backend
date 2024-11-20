from abc import ABC, abstractmethod


class LogoutPresenterInterface(ABC):
    @abstractmethod
    def success_response(self, message):
        pass
