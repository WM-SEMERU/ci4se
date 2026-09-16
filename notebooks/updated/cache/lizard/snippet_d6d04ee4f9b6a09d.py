def calc_structured_append_parity(content):
    if not isinstance(content, str_type):
        content = str(content)
    try:
        data = content.encode('iso-8859-1')
    except UnicodeError:
        try:
            data = content.encode('shift-jis')
        except (LookupError, UnicodeError):
            data = content.encode('utf-8')
    if _PY2:
        data = (ord(c) for c in data)
    return reduce(xor, data)