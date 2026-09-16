def getsize(self, path):
    try:
        file_obj = self.filesystem.resolve(path)
        if self.filesystem.ends_with_path_separator(path) and S_IFMT(file_obj
            .st_mode) != S_IFDIR:
            error_nr = (errno.EINVAL if self.filesystem.is_windows_fs else
                errno.ENOTDIR)
            self.filesystem.raise_os_error(error_nr, path)
        return file_obj.st_size
    except IOError as exc:
        raise os.error(exc.errno, exc.strerror)