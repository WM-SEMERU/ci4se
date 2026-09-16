def _fdopen_ver2(self, file_des, mode='r', bufsize=None):
    if not is_int_type(file_des):
        raise TypeError('an integer is required')
    try:
        return FakeFileOpen(self.filesystem).call(file_des, mode=mode)
    except IOError as exc:
        self.filesystem.raise_os_error(exc.errno, exc.filename)