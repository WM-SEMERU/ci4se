def asnum(number, limit=None, return_format=None):
    uri = 'asnum/{number}'.format(number=number)
    if limit:
        uri = '/'.join([uri, str(limit)])
    return _get(uri, return_format)