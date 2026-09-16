def flush(self):
    for fp in self.files:
        fp.flush()
        if isinstance(fp, int) or hasattr(fp, 'fileno'):
            try:
                os.fsync(fp)
            except OSError:
                pass