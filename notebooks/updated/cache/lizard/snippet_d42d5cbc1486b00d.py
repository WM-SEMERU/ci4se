def _parse_non_negative_int(self, istr, name):
    if istr == '':
        return None
    try:
        i = int(istr)
    except ValueError:
        raise ValueError('Failed to extract integer value for %s' % name)
    if i < 0:
        raise ValueError('Illegal negative value for %s' % name)
    return i