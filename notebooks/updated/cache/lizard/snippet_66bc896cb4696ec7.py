def file(cls, path, encoding=None, parser=None):
    cls.__hierarchy.append(file.File(path, encoding, parser))