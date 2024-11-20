import pytest
from niat_auth.tests.factory_boy_models import UserFactory
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_creation():
    user = UserFactory(username='test_user')
    assert user.username == 'test_user'
    assert user.check_password('password123')
    assert isinstance(user, User)
