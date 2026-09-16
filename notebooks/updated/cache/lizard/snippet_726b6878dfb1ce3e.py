def decoded(text, encoding=DEFAULT_ENCODING):
    if type(text) == unicode_type:
        return text
    elif type(text) != bytes_type:
        try:
            return unicode_type(text)
        except StandardError:
            try:
                text = bytes_type(text)
            except StandardError:
                msg = '<< projex.text.decoded: unable to decode ({0})>>'
                return msg.format(repr(text))
    if encoding:
        try:
            return text.decode(encoding)
        except StandardError:
            pass
    for enc in SUPPORTED_ENCODINGS:
        try:
            return text.decode(enc)
        except StandardError:
            pass
    return '????'