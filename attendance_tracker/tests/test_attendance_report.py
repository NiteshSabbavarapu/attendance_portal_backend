import json

import pytest

from attendance_tracker.interactors.attendance_report_interactor import \
    AttendanceReportInteractor
from attendance_tracker.presenters.AttendaceReportPresenterImplementation import \
    AttendanceReportPresenterImplementation
from niat_auth.tests.factory_boy_models import (AuthTokenFactory,
                                                AttendancePunchInFactory,
                                                AttendancePunchOutFactory)
from attendance_tracker.storage.AttendaceReportStorageImplementation import \
    AttendanceReportStorageImplementation


@pytest.mark.django_db
def test_get_user_attendance():
    token = AuthTokenFactory()
    AttendancePunchInFactory(user=token)
    AttendancePunchOutFactory(user=token)

    storage = AttendanceReportStorageImplementation()
    attendance_history = storage.get_user_attendance(user_id=token.user.id,
                                                     date='2024-11-18')

    assert len(attendance_history) == 1
    assert attendance_history[0]['user_id'] == token.user.id
    assert attendance_history[0]['note_of_the_day'] == "Completed work"
    assert attendance_history[0]['punch_in'] is not None
    assert attendance_history[0]['punch_out'] is not None


@pytest.mark.django_db
def test_get_recent_attendance_history():
    token = AuthTokenFactory()
    AttendancePunchInFactory(user=token)
    AttendancePunchOutFactory(user=token)

    storage = AttendanceReportStorageImplementation()
    presenter = AttendanceReportPresenterImplementation()
    interactor = AttendanceReportInteractor(storage=storage,
                                            presenter=presenter)

    response = interactor.get_recent_attendance_history(user_id=token.user.id,
                                                        date='2024-11-18')
    assert response.status_code == 200

    response_data = json.loads(response.content.decode('utf-8'))

    assert 'recent_attendance_history' in response_data
    assert len(response_data['recent_attendance_history']) == 1
    assert response_data['recent_attendance_history'][0][
               'user_id'] == token.user.id
    assert response_data['recent_attendance_history'][0][
               'note_of_the_day'] == "Completed work"
