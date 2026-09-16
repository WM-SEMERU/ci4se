def location(self):
    if self._location is None:
        self._location = '{}/{}-{}'.format(self.stream, self.type, self.
            sequence)
    return self._location