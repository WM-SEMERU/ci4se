def load(name, path=None, ext='dat', silent=False):
    filename = __get_filename(path, name, ext)
    if not os.path.exists(filename):
        if not silent:
            raise ValueException("Specified input filename doesn't exist.")
        return None
    with open(filename, 'rb') as f:
        return pickle.load(f)