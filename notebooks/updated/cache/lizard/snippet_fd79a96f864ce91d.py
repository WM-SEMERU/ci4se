def python_parser(self, obj, *args):
    attr, args = args[0], args[1:]
    item = getattr(obj, attr)
    if callable(item):
        item = item(*args)
    return [item]