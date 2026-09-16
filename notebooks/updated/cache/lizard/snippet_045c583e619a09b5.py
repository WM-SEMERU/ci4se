def _parse_field(self):
    name = self._next_token()
    if self._next_token() == '=':
        value = self._parse_value()
        return name, value