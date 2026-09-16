def _HashRow(cls, row):
    values = []
    for value in row:
        try:
            value = '{0!s}'.format(value)
        except UnicodeDecodeError:
            value = repr(value)
        values.append(value)
    return hash(' '.join(values))