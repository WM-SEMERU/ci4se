def load_include_path(paths):
    for path in paths:
        if not os.path.isdir(path):
            continue
        if path not in sys.path:
            sys.path.insert(1, path)
        for f in os.listdir(path):
            fpath = os.path.join(path, f)
            if os.path.isdir(fpath):
                load_include_path([fpath])