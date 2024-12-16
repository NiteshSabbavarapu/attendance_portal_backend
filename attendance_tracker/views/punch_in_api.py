from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from oauth2_provider.models import AccessToken
from rest_framework import status
from rest_framework.decorators import api_view

from attendance_tracker.presenters.PunchInPresenterImplementation import \
    PunchInPresenterImplementation
from attendance_tracker.storage.PunchInStorageImplementation import \
    PunchInStorageImplementation
from attendance_tracker.interactors.punch_in_interactor import PunchInInteractor
from niat_auth.models import User
from django.utils import timezone


@api_view(['POST'])
def punch_in_api(request):
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

    storage = PunchInStorageImplementation()
    presenter = PunchInPresenterImplementation()
    interactor = PunchInInteractor(storage=storage, presenter=presenter)

    interactor.mark_absent_if_no_punch_in(user.id)

    response = interactor.punch_in(user_id=user.id)
    return response
