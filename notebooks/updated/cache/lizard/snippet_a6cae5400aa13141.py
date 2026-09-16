def standard_reader_routine(reader, filename, attrs=None):
    if attrs is None:
        attrs = {}
    if not isinstance(attrs, dict):
        raise TypeError(
            'Attributes must be a dictionary of name and arguments.')
    reader.SetFileName(filename)
    for name, args in attrs.items():
        attr = getattr(reader, name)
        if args is not None:
            if not isinstance(args, (list, tuple)):
                args = [args]
            attr(*args)
        else:
            attr()
    reader.Update()
    return vtki.wrap(reader.GetOutputDataObject(0))