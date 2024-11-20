from niat_auth.exceptions.custom_exceptions import TokenNotFoundException, \
    TokenExpiredException
from niat_auth.presenter_file.refresh_token_presenter import \
    RefreshTokenPresenter
from niat_auth.stroage_file.refresh_token_storage import RefreshTokenStorage


class RefreshTokenInteractor:
    def __init__(self, storage: RefreshTokenStorage,
                 presenter: RefreshTokenPresenter):
        self.storage = storage
        self.presenter = presenter

    def refresh_token(self, data):
        token = self.storage.get_token_by_refresh(data['refresh_token'])
        if not token:
            raise TokenNotFoundException("Refresh token not found")
        if token.has_expired():
            raise TokenExpiredException("Refresh token has expired")

        new_access_token = self.storage.create_new_access_token(token)
        return self.presenter.success_response(
            {'access_token': new_access_token})
