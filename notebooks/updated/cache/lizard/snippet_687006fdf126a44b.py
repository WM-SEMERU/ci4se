def load_from_cache(path=user_path):
    if not path:
        return
    try:
        with open(path, 'rb') as f:
            dversion, mversion, data = pickle.load(f)
        if dversion == data_version and mversion == module_version:
            return data
    except (FileNotFoundError, ValueError, EOFError):
        pass