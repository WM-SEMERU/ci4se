def encode(string, encoding=None, errors=None):
    if encoding is None:
        encoding = getpreferredencoding()
    if errors is None:
        errors = getpreferrederrors()
    return string.encode(encoding, errors)