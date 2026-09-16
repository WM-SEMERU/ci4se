def list_(path, **kwargs):
    kwargs = salt.utils.args.clean_kwargs(**kwargs)
    hex_ = kwargs.pop('hex', False)
    if kwargs:
        salt.utils.args.invalid_kwargs(kwargs)
    cmd = ['xattr', path]
    try:
        ret = salt.utils.mac_utils.execute_return_result(cmd)
    except CommandExecutionError as exc:
        if 'No such file' in exc.strerror:
            raise CommandExecutionError('File not found: {0}'.format(path))
        raise CommandExecutionError('Unknown Error: {0}'.format(exc.strerror))
    if not ret:
        return {}
    attrs_ids = ret.split('\n')
    attrs = {}
    for id_ in attrs_ids:
        attrs[id_] = read(path, id_, **{'hex': hex_})
    return attrs