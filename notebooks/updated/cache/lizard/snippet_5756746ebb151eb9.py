def level(self):
    if not self._level_calculated:
        self._level_calculated = True
        self._extract_level()
    return self._level