def _find(self, index):
    match = _PATTERN.search(self.text, index)
    while self._max_tries > 0 and match is not None:
        start = match.start()
        candidate = self.text[start:match.end()]
        candidate = self._trim_after_first_match(_SECOND_NUMBER_START_PATTERN,
            candidate)
        match = self._extract_match(candidate, start)
        if match is not None:
            return match
        index = start + len(candidate)
        self._max_tries -= 1
        match = _PATTERN.search(self.text, index)
    return None