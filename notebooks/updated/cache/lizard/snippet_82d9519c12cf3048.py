def get_path(filename):
    path = abspath(filename) if os.path.isdir(filename) else dirname(abspath
        (filename))
    return path