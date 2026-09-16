def getatime(self, path):
    try:
        file_obj = self.filesystem.resolve(path)
    except IOError:
        self.filesystem.raise_os_error(errno.ENOENT)
    return file_obj.st_atime