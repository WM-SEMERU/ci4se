def get_type(full_path):
    status = {'type': []}
    if os.path.ismount(full_path):
        status['type'] += ['mount-point']
    elif os.path.islink(full_path):
        status['type'] += ['symlink']
    if os.path.isfile(full_path):
        status['type'] += ['file']
    elif os.path.isdir(full_path):
        status['type'] += ['dir']
    if not status['type']:
        if os.stat.S_ISSOCK(status['mode']):
            status['type'] += ['socket']
        elif os.stat.S_ISCHR(status['mode']):
            status['type'] += ['special']
        elif os.stat.S_ISBLK(status['mode']):
            status['type'] += ['block-device']
        elif os.stat.S_ISFIFO(status['mode']):
            status['type'] += ['pipe']
    if not status['type']:
        status['type'] += ['unknown']
    elif status['type'] and status['type'][-1] == 'symlink':
        status['type'] += ['broken']
    return status['type']