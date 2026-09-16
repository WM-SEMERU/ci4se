def create_dirs(self):
    if not os.path.isdir(self._path):
        os.makedirs(self._path)
    for dir_name in [self.OBJ_DIR, self.TMP_OBJ_DIR, self.PKG_DIR, self.
        CACHE_DIR]:
        path = os.path.join(self._path, dir_name)
        if not os.path.isdir(path):
            os.mkdir(path)
    if not os.path.exists(self._version_path()):
        self._write_format_version()