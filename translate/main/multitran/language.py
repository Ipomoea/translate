from enum import Enum


class Language(Enum):
    en = ('English', 1)
    ru = ('Russian', 2)
    de = ('German', 3)
    fr = ('French', 4)
    es = ('Spain', 5)
    it = ('Italian', 23)
    nl = ('Dutch', 24)
    lv = ('Latvian', 27)
    et = ('Estonian', 26)
    ja = ('Japanese', 28)
    af = ('African', 31)
    eo = ('Esperanto', 34)
    xal = ('Kalmyk', 35)

    @staticmethod
    def from_code(lang_code):
        for option in list(Language):
            if option.get_lang_code() == lang_code:
                return option

        raise ValueError("Invalid language code")

    def __str__(self):
        return self.value[0]

    def __repr__(self):
        return self.value[0]

    def get_code(self):
        return self.value[1]

    def get_lang_code(self):
        return self.name
