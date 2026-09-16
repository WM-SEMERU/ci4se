def WriteSymlink(self, src_arcname, dst_arcname):
    info = self._tar_fd.tarinfo()
    info.tarfile = self._tar_fd
    info.name = SmartStr(dst_arcname)
    info.size = 0
    info.mtime = time.time()
    info.type = tarfile.SYMTYPE
    info.linkname = SmartStr(src_arcname)
    self._tar_fd.addfile(info)
    return self._stream.GetValueAndReset()