def item_create(item, item_id, item_type, create='create', extra_args=None,
    cibfile=None):
    cmd = ['pcs']
    if isinstance(cibfile, six.string_types):
        cmd += ['-f', cibfile]
    if isinstance(item, six.string_types):
        cmd += [item]
    elif isinstance(item, (list, tuple)):
        cmd += item
    if item in ['constraint']:
        if isinstance(item_type, six.string_types):
            cmd += [item_type]
    if isinstance(create, six.string_types):
        cmd += [create]
    elif isinstance(create, (list, tuple)):
        cmd += create
    if item not in ['constraint']:
        cmd += [item_id]
        if isinstance(item_type, six.string_types):
            cmd += [item_type]
    if isinstance(extra_args, (list, tuple)):
        if item in ['constraint']:
            extra_args = extra_args + ['id={0}'.format(item_id)]
        cmd += extra_args
    return __salt__['cmd.run_all'](cmd, output_loglevel='trace',
        python_shell=False)