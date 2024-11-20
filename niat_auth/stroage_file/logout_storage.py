from django.core.exceptions import ObjectDoesNotExist

from niat_auth.interface_file.storage_interface.logout_storage_interface import \
    LogoutStorageInterface
from niat_auth.models import AuthToken


class LogoutStorage(LogoutStorageInterface):
    def get_token_by_access(self, access_token):
        try:
            token = AuthToken.objects.get(access_token=access_token)
        except ObjectDoesNotExist:
            return f"Access token {access_token} does not exist"
        return token

    def delete_token(self, token):
        token.delete()
