from niat_auth.exceptions.custom_exceptions import InvalidCredentialsException
from niat_auth.presenter_file.sign_in_presenter import LoginPresenter
from niat_auth.stroage_file.sign_in_storage import LoginStorage


class LoginInteractor:
    def __init__(self, storage: LoginStorage, presenter: LoginPresenter):
        self.storage = storage
        self.presenter = presenter

    def login(self, data):
        user = self.storage.authenticate_user(data['username'],
                                              data['password'])
        if not user:
            raise InvalidCredentialsException("Invalid username or password")

        token = self.storage.get_or_create_auth_token(user)
        return self.presenter.success_response({
            'access_token': token.access_token,
            'refresh_token': token.refresh_token
        })
