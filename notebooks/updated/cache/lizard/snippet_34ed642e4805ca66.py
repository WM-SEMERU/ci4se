def removedirs_p(self):
    try:
        self.removedirs()
    except OSError:
        _, e, _ = sys.exc_info()
        if e.errno != errno.ENOTEMPTY and e.errno != errno.EEXIST:
            raise
    return self