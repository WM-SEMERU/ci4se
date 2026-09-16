def value_text(self):
    search = self._selected.get()
    for item in self._rbuttons:
        if item.value == search:
            return item.text
    return ''