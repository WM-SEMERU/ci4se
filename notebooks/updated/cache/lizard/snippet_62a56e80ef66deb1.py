def find_files_for_use(self, all_files):
    for path in all_files:
        relpath = self.relpath_for(path)
        if relpath.startswith('./'):
            relpath = relpath[2:]
        if not self.is_filtered(relpath):
            yield Path(path, relpath)