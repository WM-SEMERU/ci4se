def isrc(name=None):
    if name is None:
        name = 'ISRC Field'
    field = _isrc_short(name) | _isrc_long(name)
    field.setName(name)
    return field.setResultsName('isrc')