def parse_string(data, unquote=default_unquote):
    if data is None:
        return None
    if isinstance(data, bytes):
        if sys.version_info > (3, 0, 0):
            data = data.decode('ascii')
    unquoted = unquote(data)
    if isinstance(unquoted, bytes):
        unquoted = unquoted.decode('utf-8')
    return unquoted