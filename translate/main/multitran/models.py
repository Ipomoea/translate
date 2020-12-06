class Subject:

    @property
    def name(self):
        return self._name

    @property
    def translate_options(self):
        return self._translate_options

    def __init__(self, name, translate_options):
        self._name = name
        self._translate_options = translate_options

    def __repr__(self):
        return "{name: " + self.name.__repr__() + ", translate_options: " + self.translate_options.__repr__() + "}"


class Translate:

    @property
    def subjects(self):
        return self._subjects

    def __init__(self, subjects):
        self._subjects = subjects

    def __repr__(self):
        return "{subjects: " + self.subjects + "}"
