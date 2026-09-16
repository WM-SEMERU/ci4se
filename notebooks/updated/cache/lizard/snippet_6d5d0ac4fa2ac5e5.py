def code(sentence, pad='  ', format='army'):
    try:
        return ALPHABET['code'][format](sentence, pad or CODE_PADDING[format])
    except KeyError:
        raise TypeError('Unsupported code alphabet "%s"' % (format,))