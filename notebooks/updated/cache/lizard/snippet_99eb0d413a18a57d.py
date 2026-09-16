def is_socket(self):
    try:
        return S_ISSOCK(self.stat().st_mode)
    except OSError as e:
        if e.errno not in (ENOENT, ENOTDIR):
            raise
        return False