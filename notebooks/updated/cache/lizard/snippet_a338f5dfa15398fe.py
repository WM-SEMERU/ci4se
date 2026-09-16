def parse_vars(self, args):
    result = {}
    for arg in args:
        if '=' not in arg:
            raise ValueError('Variable assignment %r invalid (no "=")' % arg)
        name, value = arg.split('=', 1)
        result[name] = value
    return result