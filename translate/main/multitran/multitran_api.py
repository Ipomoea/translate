from urllib.request import urlopen
from urllib.parse import quote, urlencode
from lxml import etree
from .models import Subject, Translate


class MultitranAPI:
    _base_url = "http://www.multitran.ru/m.exe"

    def translate(self, word, lang_origin, lang_translate):
        page = self._base_url + "?" + self._get_query(word, lang_origin, lang_translate)

        fp = urlopen(page)
        data = fp.read()

        page = data.decode("utf8")
        fp.close()

        html = etree.HTML(page)

        trs = html.xpath('//tr[td[@class="subj"]]')

        subjects = []
        for tr in trs:
            subj = tr.xpath('td[@class="subj"]/a/text()')
            text = tr.xpath('td[@class="trans"]/a/text()')

            subject = Subject(name=subj[0], translate_options=text)
            subjects.append(subject)

        return Translate(subjects=subjects)

    @staticmethod
    def _get_query(word, lang_origin, lang_translate):
        return urlencode({
            "s": quote(word),
            "l1": lang_origin.get_code(),
            "l2": lang_translate.get_code()
        })
