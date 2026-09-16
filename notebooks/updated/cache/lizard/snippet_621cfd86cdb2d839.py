def path_status(path, filename='', status=None, deep=False, verbosity=0):
    status = {} if status is None else status
    path = expand_path(path)
    if filename:
        dir_path = path
    else:
        dir_path, filename = os.path.split(path)
    full_path = os.path.join(dir_path, filename)
    if verbosity > 1:
        print('stat: {}'.format(full_path))
    status['name'] = filename
    status['path'] = full_path
    status['dir'] = dir_path
    status['type'] = []
    try:
        status.update(get_stat(full_path))
    except OSError:
        status['type'] = ['nonexistent'] + status['type']
        logger.info("Unable to stat path '{}'".format(full_path))
    status['type'] = '->'.join(status['type'])
    return status