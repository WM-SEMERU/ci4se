def current_boost_dir():
    path = os.path.dirname(os.path.realpath(__file__))
    for directory in reversed(['libs', 'mpl', 'preprocessed']):
        head, tail = os.path.split(path)
        if tail == directory:
            path = head
        else:
            return None
    return os.path.relpath(path)