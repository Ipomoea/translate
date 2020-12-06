import functools

from django.db import transaction
from django.http import JsonResponse
from django.views import View

from rest_framework import status
from rest_framework.exceptions import APIException


def base_result(json_object, status_code=status.HTTP_200_OK, error_message=None):
    """Общий ответ"""
    result = {
        "error_message": error_message,
        "status_code": status_code,
        "result": json_object
    }
    return JsonResponse(
        result,
        status=status_code,
        safe=not isinstance(json_object, list),
        json_dumps_params={
            'ensure_ascii': False,
            'indent': 2
        }
    )


def error_response(exception):
    """Формирует HTTP response с описанием ошибки"""
    if isinstance(exception, APIException):
        error_message = exception.default_detail
        status_code = exception.status_code
    else:
        error_message = str(exception)
        status_code = status.HTTP_400_BAD_REQUEST

    return base_result(None, status_code=status_code, error_message=error_message)


def base_view(fn):
    """Декоратор для всех view, обрабатывает исключения"""
    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        except Exception as e:
            return error_response(e)

    return inner


class BaseView(View):
    """Базовый класс всех view, обрабатывает исключения"""

    def dispatch(self, request, *args, **kwargs):
        try:
            return base_result(super().dispatch(request, *args, **kwargs))
        except Exception as e:
            return error_response(e)
