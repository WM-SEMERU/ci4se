def getmtime(self, path):
    try:
        file_obj = self.filesystem.resolve(path)
        return file_obj.st_mtime
    except IOError:
        self.filesystem.raise_os_error(errno.ENOENT, winerror=3)