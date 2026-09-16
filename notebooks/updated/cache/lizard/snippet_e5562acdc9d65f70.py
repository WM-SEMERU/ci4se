def listdir(self, pattern=None):
    names = os.listdir(self)
    if pattern is not None:
        names = fnmatch.filter(names, pattern)
    return [(self / child) for child in names]