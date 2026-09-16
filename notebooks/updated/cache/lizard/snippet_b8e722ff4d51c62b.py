def open_maybe_binary(filename):
    if sys.version_info >= (3, 0):
        data = open(filename, 'rb').read()
        try:
            return data.decode('utf-8')
        except UnicodeDecodeError:
            return data
    return open(filename, 'r').read()