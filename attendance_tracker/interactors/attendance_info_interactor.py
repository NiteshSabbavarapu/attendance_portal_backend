from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from oauth2_provider.models import AccessToken

from niat_auth.models import User
from attendance_tracker.storage.AttendanceInfoStorageImplementation import \
    AttendanceInfoStorageImplementation
from attendance_tracker.presenters.AttendanceInfoPresenterImplementation import \
    AttendanceInfoPresenterImplementation


class AttendanceInfoInteractor:
    def __init__(self, storage: AttendanceInfoStorageImplementation,
                 presenter: AttendanceInfoPresenterImplementation):
        self.storage = storage
        self.presenter = presenter

    def get_attendance_info(self, user_id: int, date: str):
        try:
            token = AccessToken.objects.get(user=user_id)
            if token.expires < timezone.now():
                raise Exception("Access token has expired")
        except ObjectDoesNotExist:
            raise Exception("Invalid user ID")
        attendance_data = self.storage.get_user_attendance(user_id, date)
        return self.presenter.user_attendance_percentage(attendance_data)
