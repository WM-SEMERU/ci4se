def contains(self, key):
    path = self.object_path(key)
    return os.path.exists(path) and os.path.isfile(path)