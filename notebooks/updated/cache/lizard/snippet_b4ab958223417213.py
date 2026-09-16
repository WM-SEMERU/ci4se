def token_range(self, first_token, last_token, include_extra=False):
    for i in xrange(first_token.index, last_token.index + 1):
        if include_extra or not is_non_coding_token(self._tokens[i].type):
            yield self._tokens[i]