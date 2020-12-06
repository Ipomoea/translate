from django.http import QueryDict
from django.utils.datastructures import MultiValueDictKeyError

from .translate_repository import TranslateRepository
from .multitran.language import Language
from .exceptions.exceptions import ArgumentParserError, LanguageCodeError

from core.views.base_view import BaseView


class TranslateView(BaseView):
    _repo = TranslateRepository()

    def get(self, request):
        arguments = self._parse_arguments(request)
        return self._repo.translate(arguments["word"], arguments["lang_from"], arguments["lang_to"])

    @staticmethod
    def _parse_arguments(request):
        try:
            query = QueryDict(request.META['QUERY_STRING'])

            word = query['q']
            lang_from = Language.from_code(query['lang_from'])
            lang_to = Language.from_code(query['lang_to'])

        except MultiValueDictKeyError as e:
            raise ArgumentParserError(str(e))

        except ValueError:
            raise LanguageCodeError

        return {
            "word": word,
            "lang_from": lang_from,
            "lang_to": lang_to
        }
