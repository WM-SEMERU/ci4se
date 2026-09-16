def encode_filesystem_name(input_str):
    if isinstance(input_str, str):
        input_str = unicode(input_str)
    elif not isinstance(input_str, unicode):
        raise TypeError('input_str must be a basestring')
    as_is = 'abcdefghijklmnopqrstuvwxyz0123456789.-'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    for char in input_str:
        if char in as_is:
            result.append(char)
        elif char == '_':
            result.append('__')
        elif char in uppercase:
            result.append('_%s' % char.lower())
        else:
            utf8 = char.encode('utf8')
            N = len(utf8)
            if N == 1:
                N = 0
            HH = ''.join('%x' % ord(c) for c in utf8)
            result.append('_%d%s' % (N, HH))
    return ''.join(result)