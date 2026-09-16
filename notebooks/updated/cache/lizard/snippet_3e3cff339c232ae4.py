def _realpath(path):
    if sys.platform == 'cygwin':
        if path[1:3] == ':\\':
            return path
        elif path[1:3] == ':/':
            path = '/cygdrive/' + path[0] + path[2:]
        return os.path.abspath(os.path.expanduser(path))
    return os.path.realpath(os.path.abspath(os.path.expanduser(path)))