def _get_filter_modifier(self, field):
    tokens = field.split(FIELD_SEPARATOR)
    if len(tokens) == 1:
        return field, ''
    if tokens[-1] in self.FILTER_OPERATORS.keys():
        return '.'.join(tokens[:-1]), tokens[-1]
    return '.'.join(tokens), ''