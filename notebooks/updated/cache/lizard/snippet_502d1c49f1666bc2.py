def _match_minimum_decimal(self, match_key, decimal_value, match):
    if decimal_value is None:
        raise NullArgument()
    if match is None:
        match = True
    if match:
        gtelt = '$gte'
    else:
        gtelt = '$lt'
    if match_key in self._query_terms:
        self._query_terms[match_key][gtelt] = decimal_value
    else:
        self._query_terms[match_key] = {gtelt: decimal_value}