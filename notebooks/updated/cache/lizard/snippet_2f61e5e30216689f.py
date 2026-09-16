def list_distinfo_files(self):
    base = os.path.dirname(self.path)
    for path, checksum, size in self._get_records():
        if not os.path.isabs(path):
            path = os.path.join(base, path)
        if path.startswith(self.path):
            yield path