def write_file(self, filename, **kwargs):
    with zopen(filename, 'wt') as f:
        f.write(self.get_string(**kwargs))