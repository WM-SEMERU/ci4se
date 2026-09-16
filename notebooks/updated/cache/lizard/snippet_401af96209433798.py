def _parse_next_token(self):
    while self._position < self.limit:
        token = self._next_pattern()
        if token:
            return token
    return None