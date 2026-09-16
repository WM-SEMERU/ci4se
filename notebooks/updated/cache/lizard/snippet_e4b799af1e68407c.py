def _pickle_load(path):
    _, ext = os.path.splitext(path)
    topology = None
    if sys.version_info.major == 2:
        if ext == '.pickle2':
            with open(path, 'rb') as f:
                topology = pickle.load(f)
        elif ext in ('.pickle3', '.pickle'):
            with open(path, 'rb') as f:
                topology = pickle.load(f, protocol=3)
    elif sys.version_info.major == 3:
        if ext == '.pickle2':
            with open(path, 'rb') as f:
                topology = pickle.load(f)
        elif ext in ('.pickle3', '.pickle'):
            with open(path, 'rb') as f:
                topology = pickle.load(f)
    if topology is None:
        raise ValueError('File {} is not compatible with this version'.
            format(path))
    return topology