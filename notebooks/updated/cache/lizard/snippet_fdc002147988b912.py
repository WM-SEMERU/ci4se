def files(self):
    contents = self.paths
    contents = (BinFile(path.path) for path in contents if path.is_file)
    return contents