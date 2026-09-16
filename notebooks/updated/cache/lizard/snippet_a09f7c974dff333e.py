def join(*parts, **kwargs):
    if six.PY3:
        new_parts = []
        for part in parts:
            new_parts.append(salt.utils.stringutils.to_str(part))
        parts = new_parts
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    use_posixpath = kwargs.pop('use_posixpath', False)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    pathlib = posixpath if use_posixpath else os.path
    parts = [pathlib.normpath(p) for p in parts]
    try:
        root = parts.pop(0)
    except IndexError:
        return ''
    root = salt.utils.stringutils.to_unicode(root)
    if not parts:
        ret = root
    else:
        stripped = [p.lstrip(os.sep) for p in parts]
        ret = pathlib.join(root, *salt.utils.data.decode(stripped))
    return pathlib.normpath(ret)