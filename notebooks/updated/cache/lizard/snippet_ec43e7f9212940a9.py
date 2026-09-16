def makedirs_p(self, mode=511):
    try:
        self.makedirs(mode)
    except OSError:
        _, e, _ = sys.exc_info()
        if e.errno != errno.EEXIST:
            raise
    return self