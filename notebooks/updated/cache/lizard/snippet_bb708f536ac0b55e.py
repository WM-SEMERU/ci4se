def close(self):
    if self.fp is None:
        return
    try:
        if self.mode in ('w', 'x', 'a') and self._didModify:
            with self._lock:
                if self._seekable:
                    self.fp.seek(self.start_dir)
                self._write_end_record()
    finally:
        fp = self.fp
        self.fp = None
        self._fpclose(fp)