def get_file(fn):
    fn = os.path.join(os.path.dirname(__file__), 'data', fn)
    f = open(fn, 'rb')
    lines = [line.decode('utf-8').strip() for line in f.readlines()]
    return lines