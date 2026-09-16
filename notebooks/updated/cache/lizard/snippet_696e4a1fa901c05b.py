def move(self, dst, **kwargs):
    _fs, filename = opener.parse(self.uri)
    _fs_dst, filename_dst = opener.parse(dst)
    movefile(_fs, filename, _fs_dst, filename_dst, **kwargs)
    self.uri = dst