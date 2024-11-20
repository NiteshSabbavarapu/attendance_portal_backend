from niat_auth.exceptions.custom_exceptions import TokenNotFoundException
from niat_auth.presenter_file.logout_presenter import LogoutPresenter
from niat_auth.stroage_file.logout_storage import LogoutStorage


class LogoutInteractor:
    def __init__(self, storage: LogoutStorage,
                 presenter: LogoutPresenter):
        self.storage = storage
        self.presenter = presenter

    def logout(self, data):
        token = self.storage.get_token_by_access(data.get('access_token'))
        if not token:
            raise TokenNotFoundException("Access token not found")

        self.storage.delete_token(token)
        return self.presenter.success_response("Successfully logged out")
