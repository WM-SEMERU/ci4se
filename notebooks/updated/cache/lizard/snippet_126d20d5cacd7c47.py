def to_bytes(string, encoding='utf-8', errors=None):
    unicode_name = get_canonical_encoding_name('utf-8')
    if not errors:
        if get_canonical_encoding_name(encoding) == unicode_name:
            if six.PY3 and os.name == 'nt':
                errors = 'surrogatepass'
            else:
                errors = 'surrogateescape' if six.PY3 else 'ignore'
        else:
            errors = 'strict'
    if isinstance(string, bytes):
        if get_canonical_encoding_name(encoding) == unicode_name:
            return string
        else:
            return string.decode(unicode_name).encode(encoding, errors)
    elif isinstance(string, memoryview):
        return bytes(string)
    elif not isinstance(string, six.string_types):
        try:
            if six.PY3:
                return six.text_type(string).encode(encoding, errors)
            else:
                return bytes(string)
        except UnicodeEncodeError:
            if isinstance(string, Exception):
                return b' '.join(to_bytes(arg, encoding, errors) for arg in
                    string)
            return six.text_type(string).encode(encoding, errors)
    else:
        return string.encode(encoding, errors)