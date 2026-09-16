def delimit(delimiters, content):
    if len(delimiters) != 2:
        raise ValueError('`delimiters` must be of length 2. Got %r' %
            delimiters)
    return ''.join([delimiters[0], content, delimiters[1]])