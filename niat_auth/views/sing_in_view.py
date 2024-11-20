from rest_framework.decorators import api_view

from niat_auth.interactors_file.sign_in_interactor import LoginInteractor
from niat_auth.presenter_file.sign_in_presenter import LoginPresenter
from niat_auth.stroage_file.sign_in_storage import LoginStorage


@api_view(['POST'])
def login(request):
    storage = LoginStorage()
    presenter = LoginPresenter()
    interactor = LoginInteractor(storage, presenter)
    return interactor.login(request.data)
