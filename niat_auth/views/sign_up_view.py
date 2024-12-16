from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from oauth2_provider.models import AccessToken, \
    RefreshToken, Application
from oauthlib.common import generate_token
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()


@api_view(['POST'])
def sign_up_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    student_id = request.data.get('student_id')
    phone_number = request.data.get('phone_number')

    if not all([username, password, student_id, phone_number]):
        return JsonResponse({"message": "Missing required fields."},
                            status=status.HTTP_400_BAD_REQUEST)

    try:

        if User.objects.filter(username=username).exists():
            return JsonResponse({"message": "Username already exists."},
                                status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password,
                                        student_id=student_id,
                                        phone_number=phone_number)

        application, created = Application.objects.get_or_create(
            name="1",
            client_id="636",
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_TYPES[2]
        )

        expires = now() + timedelta(days=30)
        access_token = AccessToken.objects.create(
            user=user,
            token=generate_token(),
            application=application,
            expires=expires,
            scope="read write"
        )
        refresh_token = RefreshToken.objects.create(
            user=user,
            token=generate_token(),
            application=application,
            access_token=access_token
        )

        return JsonResponse({
            "message": "User created successfully.",
            "access_token": access_token.token,
            "refresh_token": refresh_token.token,
            "expires_in": (expires - now()).seconds,
            "token_type": "Bearer"
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return JsonResponse({"message": "An error occurred: {}".format(str(e))},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
