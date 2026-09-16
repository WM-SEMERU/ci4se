def dump(filename, options, out=sys.stdout):
    with open(filename, 'rb') as file_obj:
        return _dump(file_obj, options=options, out=out)