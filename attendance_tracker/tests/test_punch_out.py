import pytest
from niat_auth.tests.factory_boy_models import AuthTokenFactory, \
    AttendancePunchOutFactory
from attendance_tracker.storage.PunchOutStorageImplementation import \
    PunchOutStorageImplementation
from attendance_tracker.presenters.PunchOutPresenterImplementation import \
    PunchOutPresenterImplementation
from attendance_tracker.interactors.punch_out_interactor import \
    PunchOutInteractor
from attendance_tracker.models import Attendance_punch_out_model
from django.utils import timezone
from datetime import timedelta


@pytest.mark.django_db
def test_punch_out_success():
    token = AuthTokenFactory()
    storage = PunchOutStorageImplementation()
    presenter = PunchOutPresenterImplementation()
    interactor = PunchOutInteractor(storage=storage, presenter=presenter)
    response = interactor.punch_out(user_id=token.user.id,
                                    note="Completed work")

    assert response.status_code == 200
    punch_out_records = Attendance_punch_out_model.objects.filter(
        user_id=token.user.id)
    assert punch_out_records.count() == 1
    assert punch_out_records[0].note_of_the_day == "Completed work"


@pytest.mark.django_db
def test_punch_out_with_expired_token():
    token = AuthTokenFactory(expires_at=timezone.now() - timedelta(days=1))
    storage = PunchOutStorageImplementation()
    presenter = PunchOutPresenterImplementation()
    interactor = PunchOutInteractor(storage=storage, presenter=presenter)

    with pytest.raises(Exception):
        interactor.punch_out(user_id=token.user.id,
                             note="Completed work")
