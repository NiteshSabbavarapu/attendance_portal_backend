from rest_framework.decorators import api_view

from niat_auth.interactors_file.sign_up_interactor import SignUpInteractor
from niat_auth.presenter_file.sign_up_presenter import SignUpPresenter
from niat_auth.stroage_file.sign_up_storage import SignUpStorage


@api_view(['POST'])
def sign_up(request):
    storage = SignUpStorage()
    presenter = SignUpPresenter()
    interactor = SignUpInteractor(storage, presenter)
    return interactor.sign_up(request.data)
