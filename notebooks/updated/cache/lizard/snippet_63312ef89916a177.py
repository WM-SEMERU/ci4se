def get_description(self, translated=False):
    if translated and self._description != '':
        return _(self._description)
    return self._description