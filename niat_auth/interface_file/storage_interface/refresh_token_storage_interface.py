from abc import ABC, abstractmethod


class RefreshTokenStorageInterface(ABC):
    @abstractmethod
    def get_token_by_refresh(self, refresh_token):
        pass

    @abstractmethod
    def create_new_access_token(self, token):
        pass
