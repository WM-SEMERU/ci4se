def decode(cls, line):
    if line.encoded:
        if 'BASE64' in line.singletonparams:
            line.singletonparams.remove('BASE64')
            line.encoding_param = cls.base64string
        encoding = getattr(line, 'encoding_param', None)
        if encoding:
            line.value = codecs.decode(line.value.encode('utf-8'), 'base64')
        else:
            line.value = stringToTextValues(line.value)[0]
        line.encoded = False