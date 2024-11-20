import pytest
from niat_auth.tests.factory_boy_models import AuthTokenFactory


@pytest.mark.django_db
def test_logout():
    token = AuthTokenFactory()
    token.delete()
    assert not AuthTokenFactory._meta.model.objects.filter(
        access_token=token.access_token).exists()
