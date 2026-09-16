def size(self):
    try:
        return os.fstat(self.file.fileno()).st_size
    except io.UnsupportedOperation:
        pass
    if is_seekable(self.file):
        with wpull.util.reset_file_offset(self.file):
            self.file.seek(0, os.SEEK_END)
            return self.file.tell()
    raise OSError('Unsupported operation.')