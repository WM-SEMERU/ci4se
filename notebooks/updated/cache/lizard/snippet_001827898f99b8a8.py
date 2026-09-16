def stream(input, encoding=None, errors='strict'):
    input = (i for i in input if i)
    if encoding:
        input = iterencode(input, encoding, errors=errors)
    return input