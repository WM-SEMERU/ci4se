def to_unicode(text, charset=None):
    if isinstance(text, str):
        try:
            return unicode(text, charset or 'utf-8')
        except UnicodeDecodeError:
            return unicode(text, 'latin1')
    elif isinstance(text, Exception):
        if os.name == 'nt' and isinstance(text, (OSError, IOError)):
            try:
                return unicode(str(text), 'mbcs')
            except UnicodeError:
                pass
        try:
            return unicode(text)
        except UnicodeError:
            return ' '.join([to_unicode(arg) for arg in text.args])
    return unicode(text)