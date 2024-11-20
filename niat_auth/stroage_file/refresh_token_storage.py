from django.core.exceptions import ObjectDoesNotExist

from niat_auth.interface_file.storage_interface.refresh_token_storage_interface import \
    RefreshTokenStorageInterface
from niat_auth.models import AuthToken
from django.utils import timezone


class RefreshTokenStorage(RefreshTokenStorageInterface):
    def get_token_by_refresh(self, refresh_token):
        try:
            token = AuthToken.objects.get(refresh_token=refresh_token)
        except ObjectDoesNotExist:
            return f"Refresh token {refresh_token} does not exist"
        return token

    def create_new_access_token(self, token):
        token.access_token = AuthToken.generate_token()
        token.expires_at = AuthToken.get_expiry()
        token.save()
        return token.access_token
