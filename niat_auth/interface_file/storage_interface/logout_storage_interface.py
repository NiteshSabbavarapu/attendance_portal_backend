from abc import ABC, abstractmethod


class LogoutStorageInterface(ABC):
    @abstractmethod
    def get_token_by_access(self, access_token):
        pass

    @abstractmethod
    def delete_token(self, token):
        pass
