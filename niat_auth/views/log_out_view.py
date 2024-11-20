from rest_framework.decorators import api_view

from niat_auth.interactors_file.logout_interactor import LogoutInteractor
from niat_auth.presenter_file.logout_presenter import LogoutPresenter
from niat_auth.stroage_file.logout_storage import LogoutStorage


@api_view(['POST'])
def logout(request):
    storage = LogoutStorage()
    presenter = LogoutPresenter()
    interactor = LogoutInteractor(storage, presenter)
    return interactor.logout(request.data)
