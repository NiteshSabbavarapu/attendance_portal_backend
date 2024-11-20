from rest_framework.response import Response
from rest_framework import status

from niat_auth.interface_file.presenter_interface.logout_presenter_interface import \
    LogoutPresenterInterface


class LogoutPresenter(LogoutPresenterInterface):
    def success_response(self, message):
        return Response({"detail": message}, status=status.HTTP_200_OK)

