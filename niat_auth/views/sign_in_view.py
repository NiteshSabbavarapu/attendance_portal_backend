from django.http import JsonResponse
from django.contrib.auth import authenticate
from oauth2_provider.models import AccessToken, RefreshToken, Application
from oauthlib.common import generate_token
from rest_framework import status
from datetime import timedelta
from django.utils.timezone import now
from rest_framework.decorators import api_view


@api_view(['POST'])
def sign_in_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return JsonResponse({"message": "Missing required fields."},
                            status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return JsonResponse({"message": "Invalid credentials."},
                            status=status.HTTP_401_UNAUTHORIZED)

    application, created = Application.objects.get_or_create(
        name="1",
        client_id="636",
        client_type=Application.CLIENT_CONFIDENTIAL,
        authorization_grant_type=Application.GRANT_TYPES[2]
    )

    access_token = AccessToken.objects.filter(
        user=user,
        application=application
    ).first()

    if access_token and access_token.expires > now():
        return JsonResponse({
            "message": "Login successful.",
            "access_token": access_token.token,
            "refresh_token": access_token.refresh_token.token,
            "expires_in": (access_token.expires - now()).seconds
        }, status=status.HTTP_200_OK)

    refresh_token = RefreshToken.objects.filter(
        user=user,
        application=application
    ).first()

    if refresh_token:
        access_token = AccessToken.objects.create(
            user=user,
            application=application,
            expires=now() + timedelta(days=30),
            token=generate_token()
        )
        return JsonResponse({
            "message": "New access token generated from refresh token.",
            "access_token": access_token.token,
            "refresh_token": refresh_token.token,
            "expires_in": (access_token.expires - now()).seconds
        }, status=status.HTTP_200_OK)

    access_token = AccessToken.objects.create(
        user=user,
        application=application,
        expires=now() + timedelta(days=30),
        token=generate_token()
    )

    refresh_token = RefreshToken.objects.create(
        user=user,
        application=application,
        token=generate_token(),
        access_token=access_token
    )

    return JsonResponse({
        "message": "Both access and refresh tokens were expired. New tokens created.",
        "access_token": access_token.token,
        "refresh_token": refresh_token.token,
        "expires_in": (access_token.expires - now()).seconds
    }, status=status.HTTP_200_OK)
