from django.contrib.auth import authenticate

from niat_auth.interface_file.storage_interface.sign_in_storage_interface import \
    LoginStorageInterface
from niat_auth.models import AuthToken


class LoginStorage(LoginStorageInterface):
    def authenticate_user(self, username, password):
        return authenticate(username=username, password=password)

    def get_or_create_auth_token(self, user):
        token, created = AuthToken.objects.get_or_create(user=user)
        if token.has_expired():
            token.delete()
            return self.create_auth_token(user)
        return token

    def create_auth_token(self, user):
        return AuthToken.objects.create(
            user=user,
            access_token=AuthToken.generate_token(),
            refresh_token=AuthToken.generate_token(),
            expires_at=AuthToken.get_expiry()
        )
