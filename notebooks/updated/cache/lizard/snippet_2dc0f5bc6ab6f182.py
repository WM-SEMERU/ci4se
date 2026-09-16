def get_token_from_offset(self, offset):
    return self._tokens[bisect.bisect(self._token_offsets, offset) - 1]