from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from oauth2_provider.models import AccessToken
from rest_framework import status

from attendance_tracker.storage.PunchInStorageImplementation import \
    PunchInStorageImplementation
from attendance_tracker.presenters.PunchInPresenterImplementation import \
    PunchInPresenterImplementation
from niat_auth.models import User
from django.utils import timezone


class PunchInInteractor:
    def __init__(self, storage: PunchInStorageImplementation,
                 presenter: PunchInPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def punch_in(self, user_id: int):
        try:
            token = AccessToken.objects.get(user=user_id)
        except ObjectDoesNotExist:
            raise Exception("Invalid user ID")

        if token.expires < timezone.now():
            raise Exception("Access token has expired")

        punch_in_instance = self.storage.create_punch_in(user_id)

        if "you have already punched in" in punch_in_instance:
            return JsonResponse(
                {"message": punch_in_instance},
                status=status.HTTP_200_OK
            )
        if punch_in_instance is None:
            return JsonResponse(
                {"message": "No punch-in required today (Holiday or Late)."},
                status=status.HTTP_200_OK)
        if punch_in_instance == "Absent":
            return JsonResponse(
                {"message": "You are absent today"},
                status=status.HTTP_200_OK
            )

        return self.presenter.punch_in_attendance_response(punch_in_instance)

    def mark_absent_if_no_punch_in(self, user_id: int):
        self.storage.mark_absent_for_no_punch_in(user_id)
