from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from oauth2_provider.models import AccessToken
from rest_framework import status
from rest_framework.decorators import api_view

from attendance_tracker.presenters.PunchOutPresenterImplementation import \
    PunchOutPresenterImplementation
from attendance_tracker.storage.PunchOutStorageImplementation import \
    PunchOutStorageImplementation
from attendance_tracker.interactors.punch_out_interactor import \
    PunchOutInteractor
from niat_auth.models import User
from django.utils import timezone


@api_view(['POST'])
def punch_out_api(request):
    auth_token = request.data.get('access_token')
    note = request.data.get('note_of_the_day', "")

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

    storage = PunchOutStorageImplementation()
    presenter = PunchOutPresenterImplementation()
    interactor = PunchOutInteractor(storage=storage, presenter=presenter)

    response = interactor.punch_out(user_id=user.id, note=note)
    return response
