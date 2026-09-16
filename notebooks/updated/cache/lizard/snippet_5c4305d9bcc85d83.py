def source_lines(self, filename):
    with self.filesystem.open(filename) as f:
        return f.readlines()