from django.http import JsonResponse
from oauth2_provider.models import AccessToken, RefreshToken
from rest_framework import status
from django.utils.timezone import now
from rest_framework.decorators import api_view


@api_view(['POST'])
def sign_out_view(request):
    access_token = request.data.get('access_token')
    refresh_token = request.data.get('refresh_token')

    if not access_token or not refresh_token:
        return JsonResponse({"message": "Missing required fields."},
                            status=status.HTTP_400_BAD_REQUEST)

    AccessToken.objects.filter(token=access_token).delete()
    RefreshToken.objects.filter(token=refresh_token).delete()

    return JsonResponse({"message": "Logout successful."},
                        status=status.HTTP_200_OK)
