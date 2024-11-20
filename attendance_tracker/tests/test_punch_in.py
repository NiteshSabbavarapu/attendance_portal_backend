import pytest
from niat_auth.tests.factory_boy_models import AuthTokenFactory, \
    AttendancePunchInFactory
from attendance_tracker.storage.PunchInStorageImplementation import \
    PunchInStorageImplementation
from attendance_tracker.presenters.PunchInPresenterImplementation import \
    PunchInPresenterImplementation
from attendance_tracker.interactors.punch_in_interactor import PunchInInteractor
from attendance_tracker.models import Attendance_punch_in_model
from django.utils import timezone
from datetime import timedelta


@pytest.mark.django_db
def test_punch_in_success():
    token = AuthTokenFactory()
    storage = PunchInStorageImplementation()
    presenter = PunchInPresenterImplementation()
    interactor = PunchInInteractor(storage=storage, presenter=presenter)
    response = interactor.punch_in(user_id=token.user.id)

    assert response.status_code == 200
    punch_in_records = Attendance_punch_in_model.objects.filter(
        user_id=token.user.id)
    assert punch_in_records.count() == 1
    assert punch_in_records[0].attendance_status == "Present"


@pytest.mark.django_db
def test_punch_in_with_expired_token():
    token = AuthTokenFactory(expires_at=timezone.now() - timedelta(days=1))
    storage = PunchInStorageImplementation()
    presenter = PunchInPresenterImplementation()
    interactor = PunchInInteractor(storage=storage, presenter=presenter)

    with pytest.raises(Exception):
        interactor.punch_in(user_id=token.user.id)
