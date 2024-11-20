from abc import ABC, abstractmethod


class RefreshTokenPresenterInterface(ABC):
    @abstractmethod
    def success_response(self, data):
        pass

    @abstractmethod
    def error_response(self, message):
        pass
