def beststr(*strings):
    for x in strings:
        try:
            x.encode(sys.stdout.encoding)
        except UnicodeEncodeError:
            pass
        else:
            return x
    raise ValueError('No valid strings found')