from niat_auth.exceptions.custom_exceptions import UserCreationFailedException
from niat_auth.presenter_file.sign_up_presenter import SignUpPresenter
from niat_auth.stroage_file.sign_up_storage import SignUpStorage


class SignUpInteractor:
    def __init__(self, storage: SignUpStorage,
                 presenter: SignUpPresenter):
        self.storage = storage
        self.presenter = presenter

    def sign_up(self, data):
        user = self.storage.create_user(data)
        if not user:
            return UserCreationFailedException("User creation failed")

        token = self.storage.create_auth_token(user)
        return self.presenter.success_response({
            'access_token': token.access_token,
            'refresh_token': token.refresh_token
        })
