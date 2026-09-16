def dot_mavproxy(name=None):
    if 'HOME' not in os.environ:
        dir = os.path.join(os.environ['LOCALAPPDATA'], '.mavproxy')
    else:
        dir = os.path.join(os.environ['HOME'], '.mavproxy')
    mkdir_p(dir)
    if name is None:
        return dir
    return os.path.join(dir, name)