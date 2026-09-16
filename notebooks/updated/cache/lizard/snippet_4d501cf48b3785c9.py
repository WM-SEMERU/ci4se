def rmdir_p(self):
    suppressed = FileNotFoundError, FileExistsError, DirectoryNotEmpty
    with contextlib.suppress(suppressed):
        with DirectoryNotEmpty.translate():
            self.rmdir()
    return self