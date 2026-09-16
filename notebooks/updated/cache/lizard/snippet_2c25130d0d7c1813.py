def _parse_literal_list(self, indent):
    if self._cur_token['type'] not in self._literals:
        raise Exception(
            'Parser failed, _parse_literal_list was called on non-literal {} on line {}.'
            .format(repr(self._cur_token['value']), self._cur_token['line']))
    temp_position = self._cur_position
    while temp_position < self.num_tokens - 1 and (self.tokens[
        temp_position]['type'] is TT.ws or self.tokens[temp_position][
        'type'] in self._literals):
        temp_position += 1
    next_token = self.tokens[temp_position]
    if next_token['type'] is TT.ws:
        return self._cur_token['value']
    elif next_token['type'] is TT.comma:
        return self._parse_comma_list()
    elif next_token['type'] is TT.lbreak:
        while temp_position < self.num_tokens - 1 and self.tokens[temp_position
            ]['type'] in (TT.lbreak, TT.ws):
            temp_position += 1
        if self.tokens[temp_position]['type'] in self._literals:
            return self._parse_newline_list(indent)
        else:
            rval = self._cur_token['value']
            self._increment()
            return rval
    else:
        rval = self._cur_token['value']
        self._increment()
        return rval