def _extract_file(self, tgz, tarinfo, dst_path, buffer_size=10 << 20):
    src = tgz.extractfile(tarinfo)
    dst = tf_v1.gfile.GFile(dst_path, 'wb')
    while 1:
        buf = src.read(buffer_size)
        if not buf:
            break
        dst.write(buf)
        self._log_progress(len(buf))
    dst.close()
    src.close()