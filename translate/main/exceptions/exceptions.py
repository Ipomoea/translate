from rest_framework import status
from rest_framework.exceptions import APIException


class ArgumentParserError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "Missing expected arguments"

    def __init__(self, description):
        if description:
            self.default_detail += f" ({description})"


class TranslateRepositoryError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Couldn't get remote translate"


class LanguageCodeError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = "Invalid language code"
