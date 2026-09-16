def _encode_status(status):
    if six.PY2:
        return status
    if not isinstance(status, str):
        raise TypeError('WSGI response status is not of type str.')
    return status.encode('ISO-8859-1')