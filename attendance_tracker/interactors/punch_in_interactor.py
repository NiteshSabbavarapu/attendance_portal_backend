from django.core.exceptions import ObjectDoesNotExist

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
        punch_in_instance = self.storage.create_punch_in(user_id)
        if punch_in_instance is None:
            raise Exception("Punch in failed")

        return self.presenter.punch_in_attendance_response(punch_in_instance)
