from django.utils import timezone

from attendance_tracker.storage.PunchOutStorageImplementation import (
    PunchOutStorageImplementation)
from attendance_tracker.presenters.PunchOutPresenterImplementation import (
    PunchOutPresenterImplementation)
from niat_auth.models import AuthToken


class PunchOutInteractor:
    def __init__(self, storage: PunchOutStorageImplementation,
                 presenter: PunchOutPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def punch_out(self, user_id: int, note: str):
        token = AuthToken.objects.get(user_id=user_id)
        if token.expires_at < timezone.now():
            raise Exception("Access token has expired")
        punch_out_instance = self.storage.create_punch_out(user_id, note)
        return self.presenter.punch_out_attendance_response(punch_out_instance)
