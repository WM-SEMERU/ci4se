def ustr(text):
    if text is not None:
        if sys.version_info >= (3, 0):
            return str(text)
        else:
            return unicode(text)
    else:
        return text