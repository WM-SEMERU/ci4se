def open(self, file, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None):
    if opener is not None and sys.version_info < (3, 3):
        raise TypeError("open() got an unexpected keyword argument 'opener'")
    fake_open = FakeFileOpen(self.filesystem, use_io=True)
    return fake_open(file, mode, buffering, encoding, errors, newline,
        closefd, opener)