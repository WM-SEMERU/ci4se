def get_name(self, language):
    return self.gettext(language, self._name) if self._name else ''