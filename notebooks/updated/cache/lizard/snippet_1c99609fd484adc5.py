def _Comparator(self, operator):
    if operator == '=':
        return lambda x, y: x == y
    elif operator == '>=':
        return lambda x, y: x >= y
    elif operator == '>':
        return lambda x, y: x > y
    elif operator == '<=':
        return lambda x, y: x <= y
    elif operator == '<':
        return lambda x, y: x < y
    elif operator == '!':
        return lambda x, y: x != y
    raise DefinitionError('Invalid comparison operator %s' % operator)