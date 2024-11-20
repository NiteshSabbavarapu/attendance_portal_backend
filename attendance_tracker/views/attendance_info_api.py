from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from attendance_tracker.presenters.AttendanceInfoPresenterImplementation import \
    AttendanceInfoPresenterImplementation
from attendance_tracker.storage.AttendanceInfoStorageImplementation import \
    AttendanceInfoStorageImplementation
from attendance_tracker.interactors.attendance_info_interactor import \
    AttendanceInfoInteractor
from niat_auth.models import AuthToken
from django.utils import timezone


@api_view(['POST'])
def attendance_info_home_page_api(request):
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
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Invalid access token."},
                            status=status.HTTP_401_UNAUTHORIZED)

    storage = AttendanceInfoStorageImplementation()
    presenter = AttendanceInfoPresenterImplementation()
    interactor = AttendanceInfoInteractor(storage=storage, presenter=presenter)

    response = interactor.get_attendance_info(user_id=user.id, date=date)
    return response
