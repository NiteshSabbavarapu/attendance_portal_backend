import pytest
from niat_auth.tests.factory_boy_models import AuthTokenFactory
from datetime import timedelta
from django.utils import timezone


@pytest.mark.django_db
def test_refresh_token_valid():
    token = AuthTokenFactory()
    assert token.expires_at > timezone.now()
    new_access_token = AuthTokenFactory().access_token
    assert new_access_token != token.access_token


@pytest.mark.django_db
def test_refresh_token_expired():
    token = AuthTokenFactory(expires_at=timezone.now() - timedelta(days=1))
    assert token.expires_at < timezone.now()
