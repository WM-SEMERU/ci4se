def stat(self, path):
    try:
        stat = self.exists(str(path))
    except (NoNodeError, NoAuthError):
        stat = None
    return stat