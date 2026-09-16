def collapseuser(path):
    home = os.path.join(os.path.expanduser('~'), '')
    if path.startswith(home):
        path = os.path.join('~', path[len(home):])
    return path