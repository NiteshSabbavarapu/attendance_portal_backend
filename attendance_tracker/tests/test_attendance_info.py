import json

import pytest
from niat_auth.tests.factory_boy_models import AuthTokenFactory, \
    AttendancePunchInFactory
from attendance_tracker.storage.AttendanceInfoStorageImplementation import \
    AttendanceInfoStorageImplementation
from attendance_tracker.presenters.AttendanceInfoPresenterImplementation import \
    AttendanceInfoPresenterImplementation
from attendance_tracker.interactors.attendance_info_interactor import \
    AttendanceInfoInteractor


@pytest.mark.django_db
def test_get_attendance_info_success():
    token = AuthTokenFactory()

    AttendancePunchInFactory(user=token)
    AttendancePunchInFactory(user=token)

    storage = AttendanceInfoStorageImplementation()
    presenter = AttendanceInfoPresenterImplementation()
    interactor = AttendanceInfoInteractor(storage=storage, presenter=presenter)

    attendance_data = interactor.get_attendance_info(user_id=token.user.id,
                                                     date='2024-11-18')

    assert attendance_data.status_code == 200


@pytest.mark.django_db
def test_get_attendance_info_no_attendance():
    token = AuthTokenFactory()
    storage = AttendanceInfoStorageImplementation()
    presenter = AttendanceInfoPresenterImplementation()
    interactor = AttendanceInfoInteractor(storage=storage, presenter=presenter)

    response = interactor.get_attendance_info(user_id=token.user.id,
                                              date='2024-11-18')

    response_data = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert response_data['user_attendance_percentage'] == 0
    assert response_data['present_days'] == 0
    assert response_data['absent_days'] > 0
    assert response_data['remaining_days'] > 0


@pytest.mark.django_db
def test_attendance_info_invalid_token():
    storage = AttendanceInfoStorageImplementation()
    presenter = AttendanceInfoPresenterImplementation()
    interactor = AttendanceInfoInteractor(storage=storage, presenter=presenter)

    with pytest.raises(Exception):
        interactor.get_attendance_info(user_id=999,
                                       date='2024-11-18')
