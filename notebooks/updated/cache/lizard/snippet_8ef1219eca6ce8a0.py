def relpath_for(self, path):
    if self.parent_dir in ('.', ''):
        return path
    if path == self.parent_dir:
        return ''
    dirname = os.path.dirname(path) or '.'
    basename = os.path.basename(path)
    cached = self.relpath_cache.get(dirname, empty)
    if cached is empty:
        cached = self.relpath_cache[dirname] = os.path.relpath(dirname,
            self.parent_dir)
    return os.path.join(cached, basename)