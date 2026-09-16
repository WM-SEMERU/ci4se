def guess_minimum_encoding(text, charsets=('ascii', 'latin1', 'utf8')):
    text_in_unicode = text.decode('utf8', 'replace')
    for charset in charsets:
        try:
            return text_in_unicode.encode(charset), charset
        except (UnicodeEncodeError, UnicodeDecodeError):
            pass
    return text_in_unicode.encode('utf8'), 'utf8'