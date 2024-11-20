import factory
from django.utils import timezone
from django.contrib.auth.models import User
from niat_auth.models import AuthToken
from attendance_tracker.models import Attendance_punch_in_model, \
    Attendance_punch_out_model
import uuid
from datetime import timedelta


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    password = factory.PostGenerationMethodCall('set_password', 'password123')


class AuthTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AuthToken

    user = factory.SubFactory(UserFactory)
    access_token = factory.LazyFunction(lambda: uuid.uuid4().hex)
    refresh_token = factory.LazyFunction(lambda: uuid.uuid4().hex)
    expires_at = timezone.now() + timedelta(days=1)


class AttendancePunchInFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance_punch_in_model

    user = factory.SubFactory(AuthTokenFactory)
    attendance_status = "Present"


class AttendancePunchOutFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance_punch_out_model

    user = factory.SubFactory(AuthTokenFactory)
    note_of_the_day = "Completed work"
