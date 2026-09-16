def serialize(struct, format, target=None, encoding='utf-8'):
    if hasattr(target, 'encoding') and target.encoding:
        raise AnyMarkupError('Input file must be opened in binary mode')
    fname = None
    if hasattr(target, 'name'):
        fname = target.name
    fmt = _get_format(format, fname)
    try:
        serialized = _do_serialize(struct, fmt, encoding)
        if target is None:
            return serialized
        else:
            return target.write(serialized)
    except Exception as e:
        raise AnyMarkupError(e, traceback.format_exc())