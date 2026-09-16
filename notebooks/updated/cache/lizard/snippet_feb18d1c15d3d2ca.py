def to_unicode(str_or_unicode, precise=False):
    if not isinstance(str_or_unicode, six.text_type):
        encoding = quick_detect_encoding(str_or_unicode
            ) if precise else 'utf-8'
        return six.text_type(str_or_unicode, encoding, 'replace')
    return str_or_unicode