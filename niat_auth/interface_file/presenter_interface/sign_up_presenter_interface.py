from abc import ABC, abstractmethod


class SignUpPresenterInterface(ABC):
    @abstractmethod
    def success_response(self, data):
        pass

