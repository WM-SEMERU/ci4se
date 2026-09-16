def dirs(self):
    contents = self.paths
    contents = (BinDir(path.path) for path in contents if path.is_dir)
    return contents