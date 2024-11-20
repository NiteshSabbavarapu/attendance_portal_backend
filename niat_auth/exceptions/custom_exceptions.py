class UserCreationFailedException(Exception):
    pass


class InvalidCredentialsException(Exception):
    pass


class TokenExpiredException(Exception):
    pass


class TokenNotFoundException(Exception):
    pass


class AuthenticationFailedException(Exception):
    pass
