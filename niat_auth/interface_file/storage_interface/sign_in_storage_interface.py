from abc import ABC, abstractmethod


class LoginStorageInterface(ABC):
    @abstractmethod
    def authenticate_user(self, username, password):
        pass

    @abstractmethod
    def get_or_create_auth_token(self, user):
        pass

    @abstractmethod
    def create_auth_token(self, user):
        pass
