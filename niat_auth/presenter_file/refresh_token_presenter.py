from rest_framework.response import Response
from rest_framework import status

from niat_auth.interface_file.presenter_interface.refresh_token_presenter_interface import \
    RefreshTokenPresenterInterface


class RefreshTokenPresenter(RefreshTokenPresenterInterface):
    def success_response(self, data):
        return Response(data, status=status.HTTP_200_OK)

    def error_response(self, message):
        return Response({"detail": message},
                        status=status.HTTP_401_UNAUTHORIZED)
