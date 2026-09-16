def _native_to_unicode(s):
    if six.PY2:
        return s if isinstance(s, unicode) else s.decode('utf-8')
    else:
        return s