def choices(self):
    if isinstance(self._choices, Promise):
        self._choices = list(self._choices)
    return self._choices