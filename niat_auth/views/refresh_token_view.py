from rest_framework.decorators import api_view

from niat_auth.interactors_file.refresh_token_interactor import \
    RefreshTokenInteractor
from niat_auth.presenter_file.refresh_token_presenter import \
    RefreshTokenPresenter
from niat_auth.stroage_file.refresh_token_storage import RefreshTokenStorage


@api_view(['POST'])
def refresh_token(request):
    storage = RefreshTokenStorage()
    presenter = RefreshTokenPresenter()
    interactor = RefreshTokenInteractor(storage, presenter)
    return interactor.refresh_token(request.data)
