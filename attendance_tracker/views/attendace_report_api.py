from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from oauth2_provider.models import AccessToken
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
from niat_auth.models import User
from django.utils import timezone


@api_view(['POST'])
def attendance_report_api(request):
    auth_token = request.data.get('access_token')
    if not auth_token:
        return JsonResponse({"message": "Auth token is required."},
                            status=status.HTTP_400_BAD_REQUEST)

    try:
        token = AccessToken.objects.get(token=auth_token)
        if token.expires < timezone.now():
            return JsonResponse({"message": "Access token has expired."},
                                status=status.HTTP_401_UNAUTHORIZED)
        user = token.user
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Invalid access token."},
                            status=status.HTTP_401_UNAUTHORIZED)

    storage = AttendanceReportStorageImplementation()
    presenter = AttendanceReportPresenterImplementation()
    interactor = AttendanceReportInteractor(storage=storage,
                                            presenter=presenter)

    return interactor.get_recent_attendance_history(
        user_id=user.id)
