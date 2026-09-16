def create_directory(self, path):
    _complain_ifclosed(self.closed)
    return self.fs.create_directory(path)