from django.http import JsonResponse
from django.utils import timezone
from oauth2_provider.models import AccessToken
from rest_framework import status

from attendance_tracker.storage.PunchOutStorageImplementation import (
    PunchOutStorageImplementation)
from attendance_tracker.presenters.PunchOutPresenterImplementation import (
    PunchOutPresenterImplementation)
from niat_auth.models import User


class PunchOutInteractor:
    def __init__(self, storage: PunchOutStorageImplementation,
                 presenter: PunchOutPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def punch_out(self, user_id: int, note: str):
        token = AccessToken.objects.get(user=user_id)
        if token.expires < timezone.now():
            raise Exception("Access token has expired")
        punch_out_instance = self.storage.create_punch_out(user_id, note)
        if punch_out_instance is None:
            return JsonResponse(
                {"message": "You are absent today"},
                status=status.HTTP_200_OK
            )
        if punch_out_instance == "you have already punched out":
            return JsonResponse(
                {"message": "You have already punched out"},
                status=status.HTTP_200_OK
            )
        return self.presenter.punch_out_attendance_response(punch_out_instance)
