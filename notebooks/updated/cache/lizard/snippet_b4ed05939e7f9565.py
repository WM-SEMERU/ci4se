def delete_by_path(self, path):
    if not os.path.exists(path):
        raise IOError("Unknown path '%s'!" % path)
    if not path.startswith(self.path):
        raise IOError("Path '%s' is not in the root of the storage ('%s')!" %
            (path, self.path))
    if os.path.isfile(path):
        os.unlink(path)
        return self._recursive_remove_blank_dirs(path)
    shutil.rmtree(path)
    self._recursive_remove_blank_dirs(path)