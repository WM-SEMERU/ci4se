def write(data, path, saltenv='base', index=0):
    if saltenv not in __opts__['pillar_roots']:
        return 'Named environment {0} is not present'.format(saltenv)
    if len(__opts__['pillar_roots'][saltenv]) <= index:
        return 'Specified index {0} in environment {1} is not present'.format(
            index, saltenv)
    if os.path.isabs(path):
        return ('The path passed in {0} is not relative to the environment {1}'
            .format(path, saltenv))
    dest = os.path.join(__opts__['pillar_roots'][saltenv][index], path)
    dest_dir = os.path.dirname(dest)
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    with salt.utils.files.fopen(dest, 'w+') as fp_:
        fp_.write(salt.utils.stringutils.to_str(data))
    return 'Wrote data to file {0}'.format(dest)