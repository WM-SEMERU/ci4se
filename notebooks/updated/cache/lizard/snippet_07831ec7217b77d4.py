def chmod(self, path, mode, dir_fd=None, follow_symlinks=None):
    if follow_symlinks is None:
        follow_symlinks = True
    elif sys.version_info < (3, 3):
        raise TypeError(
            "chmod() got an unexpected keyword argument 'follow_symlinks'")
    path = self._path_with_dir_fd(path, self.chmod, dir_fd)
    self.filesystem.chmod(path, mode, follow_symlinks)