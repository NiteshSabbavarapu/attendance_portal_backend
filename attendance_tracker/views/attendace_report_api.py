from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from attendance_tracker.presenters.AttendaceReportPresenterImplementation import (
    AttendanceReportPresenterImplementation
)
from attendance_tracker.storage.AttendaceReportStorageImplementation import (
    AttendanceReportStorageImplementation
)
from attendance_tracker.interactors.attendance_report_interactor import (
    AttendanceReportInteractor
)
from niat_auth.models import AuthToken
from django.utils import timezone


@api_view(['POST'])
def attendance_report_api(request):
    auth_token = request.data.get('auth_token')
    date = request.data.get('date')

    if not auth_token or not date:
        return JsonResponse({"message": "Auth token and Date are required."},
                            status=status.HTTP_400_BAD_REQUEST)

    try:
        token = AuthToken.objects.get(access_token=auth_token)
        if token.expires_at < timezone.now():
            return JsonResponse({"message": "Access token has expired."},
                                status=status.HTTP_401_UNAUTHORIZED)
        user = token.user
    except AuthToken.DoesNotExist:
        return JsonResponse({"message": "Invalid access token."},
                            status=status.HTTP_401_UNAUTHORIZED)

    storage = AttendanceReportStorageImplementation()
    presenter = AttendanceReportPresenterImplementation()
    interactor = AttendanceReportInteractor(storage=storage,
                                            presenter=presenter)

    response = interactor.get_recent_attendance_history(user_id=user.id,
                                                        date=date)
    return response
