from .multitran.multitran_api import MultitranAPI
from .translate_storage import TranslateStorage
from .exceptions.exceptions import TranslateRepositoryError


class TranslateRepository:
    _api = MultitranAPI()
    _storage = TranslateStorage()

    def translate(self, word, lang_origin, lang_translate):
        stored_value = self._get_translates(word, lang_origin, lang_translate)
        if stored_value:
            return stored_value

        try:
            remote_value = self._api.translate(word, lang_origin, lang_translate)
        except Exception:
            raise TranslateRepositoryError

        self._storage.set_translate(word, lang_origin, lang_translate, remote_value.subjects)
        return self._get_translates(word, lang_origin, lang_translate)

    def _get_translates(self, word, lang_origin, lang_translate):
        return self._storage.get_translates(word, lang_origin, lang_translate)
