def format(self):
    name = self._primary.value[0]
    if self.surname:
        if name:
            name += ' '
        name += self.surname
    if self._primary.value[2]:
        if name:
            name += ' '
        name += self._primary.value[2]
    return name