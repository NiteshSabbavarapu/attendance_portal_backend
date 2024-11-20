from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from niat_auth.models import AuthToken
from niat_auth.interface_file.storage_interface.sign_up_storage_interface import \
    SignUpStorageInterface


class SignUpStorage(SignUpStorageInterface):
    def create_user(self, data):
        try:
            User.objects.get(username=data['username'])
        except ObjectDoesNotExist:
            return f"User with username {data['username']} does not exist"

        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        return user

    def create_auth_token(self, user):
        return AuthToken.objects.create(
            user=user,
            access_token=AuthToken.generate_token(),
            refresh_token=AuthToken.generate_token(),
            expires_at=AuthToken.get_expiry()
        )
