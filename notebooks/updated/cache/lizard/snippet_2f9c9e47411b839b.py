def pypackable(name, pytype, format):
    size, items = _formatinfo(format)
    return type(Packable)(name, (pytype, Packable), {'_format_': format,
        '_size_': size, '_items_': items})