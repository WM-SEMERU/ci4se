def DirnamePath(self, path):
    if path.endswith(self.PATH_SEPARATOR):
        path = path[:-1]
    if not path:
        return None
    dirname, _, _ = path.rpartition(self.PATH_SEPARATOR)
    return dirname