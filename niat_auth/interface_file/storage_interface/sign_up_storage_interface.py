from abc import ABC, abstractmethod


class SignUpStorageInterface(ABC):
    @abstractmethod
    def create_user(self, data):
        pass

    @abstractmethod
    def create_auth_token(self, user):
        pass
