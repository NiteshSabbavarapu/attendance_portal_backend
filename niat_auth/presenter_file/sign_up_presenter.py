from rest_framework.response import Response
from rest_framework import status

from niat_auth.interface_file.presenter_interface.sign_up_presenter_interface import \
    SignUpPresenterInterface


class SignUpPresenter(SignUpPresenterInterface):
    def success_response(self, data):
        return Response(data, status=status.HTTP_201_CREATED)
