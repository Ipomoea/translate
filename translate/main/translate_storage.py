from .models import Entry, Translate, Subject
from django.db import connection


class TranslateStorage:

    def get_translates(self, word, lang_from, lang_to):
        lang_key = self._get_lang_key(lang_from, lang_to)
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT main_translate.value AS config, main_subject.value AS subject
                    FROM main_translate 
                    LEFT JOIN main_subject ON main_translate.subject_id = main_subject.id
                    WHERE entry_id = (
                        SELECT id FROM main_entry WHERE origin = "%s" AND lang_key = "%s"
                    )
                """ % (word, lang_key)
            )
            raw_data = cursor.fetchall()

        json_data = {}
        for translate, subject in raw_data:
            if subject not in json_data:
                json_data[subject] = []
            json_data[subject].append(translate)

        return json_data

    def set_translate(self, word, lang_from, lang_to, subjects):
        lang_key = self._get_lang_key(lang_from, lang_to)

        entry = Entry.objects.create(
            origin=word,
            lang_key=lang_key
        )

        for subject in subjects:
            try:
                subject_model = Subject.objects.get(value=subject.name, lang_code=lang_to.get_lang_code())
            except Subject.DoesNotExist:
                subject_model = Subject.objects.create(value=subject.name, lang_code=lang_to.get_lang_code())

            for translate in subject.translate_options:
                Translate.objects.create(entry=entry, subject=subject_model, value=translate)

    @staticmethod
    def _get_lang_key(lang_from, lang_to):
        return lang_from.get_lang_code() + "_" + lang_to.get_lang_code()
