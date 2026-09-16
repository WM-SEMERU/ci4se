def __find_file(name, path, deep=False, partial=False):
    if deep:
        for root, dirs, files in os.walk(path):
            if partial:
                for file in files:
                    if name in file:
                        return os.path.join(root, file)
            elif name in files:
                return os.path.join(root, name)
    else:
        f = os.path.join(path, name)
        if os.path.isfile(f):
            return f