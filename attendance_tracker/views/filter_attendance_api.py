from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from attendance_tracker.presenters.AttendanceFilterPresenterImplementation import \
    AttendanceFilterPresenterImplementation
from attendance_tracker.storage.AttendanceFilterStorageImplementation import \
    AttendanceFilterStorageImplementation
from attendance_tracker.interactors.attendance_filter_interactor import \
    AttendanceFilterInteractor
from niat_auth.models import AuthToken


@api_view(['GET'])
def filter_attendance_api(request):
    auth_token = request.GET.get('auth_token')
    attendance_status = request.GET.get('status')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if not auth_token:
        return JsonResponse({"message": "Auth token is required."},
                            status=status.HTTP_400_BAD_REQUEST)

    try:
        token = AuthToken.objects.get(access_token=auth_token)
        user_id = token.user.id
    except ObjectDoesNotExist:
        return JsonResponse({"message": "Invalid auth token."},
                            status=status.HTTP_401_UNAUTHORIZED)

    storage = AttendanceFilterStorageImplementation()
    presenter = AttendanceFilterPresenterImplementation()
    interactor = AttendanceFilterInteractor(storage=storage,
                                            presenter=presenter)
    response = interactor.filter_attendance(user_id=user_id,
                                            status=attendance_status,
                                            start_date=start_date,
                                            end_date=end_date)
    return response
