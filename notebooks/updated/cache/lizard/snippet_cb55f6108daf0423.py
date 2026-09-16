def safe_str(unicode_, to_encoding=None):
    if not isinstance(unicode_, basestring):
        return str(unicode_)
    if isinstance(unicode_, str):
        return unicode_
    if not to_encoding:
        from vcs.conf import settings
        to_encoding = settings.DEFAULT_ENCODINGS
    if not isinstance(to_encoding, (list, tuple)):
        to_encoding = [to_encoding]
    for enc in to_encoding:
        try:
            return unicode_.encode(enc)
        except UnicodeEncodeError:
            pass
    try:
        import chardet
        encoding = chardet.detect(unicode_)['encoding']
        if encoding is None:
            raise UnicodeEncodeError()
        return unicode_.encode(encoding)
    except (ImportError, UnicodeEncodeError):
        return unicode_.encode(to_encoding[0], 'replace')
    return safe_str