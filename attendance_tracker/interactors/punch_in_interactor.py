from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status

from attendance_tracker.storage.PunchInStorageImplementation import \
    PunchInStorageImplementation
from attendance_tracker.presenters.PunchInPresenterImplementation import \
    PunchInPresenterImplementation
from niat_auth.models import AuthToken
from django.utils import timezone


class PunchInInteractor:
    def __init__(self, storage: PunchInStorageImplementation,
                 presenter: PunchInPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def punch_in(self, user_id: int):
        try:
            token = AuthToken.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            raise Exception("Invalid user ID")
        if token.expires_at < timezone.now():
            raise Exception("Access token has expired")

        # Create punch-in entry
        punch_in_instance = self.storage.create_punch_in(user_id)
        if punch_in_instance is None:
            return JsonResponse(
                {"message": "No punch-in required today (Holiday or Late)."},
                status=status.HTTP_200_OK)

        return self.presenter.punch_in_attendance_response(punch_in_instance)

    def mark_absent_if_no_punch_in(self, user_id: int):
        self.storage.mark_absent_for_no_punch_in(user_id)
