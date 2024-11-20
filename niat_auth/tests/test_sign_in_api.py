import pytest
from niat_auth.tests.factory_boy_models import UserFactory, AuthTokenFactory


@pytest.mark.django_db
def test_valid_login():
    user = UserFactory(username='testuser', password='password123')
    token = AuthTokenFactory(user=user)
    assert token.user.username == 'testuser'
    assert len(token.access_token) > 0
    assert len(token.refresh_token) > 0


@pytest.mark.django_db
def test_invalid_login():
    user = UserFactory(username='testuser', password='password123')
    assert not user.check_password('wrongpassword')
