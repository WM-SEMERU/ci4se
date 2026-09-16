def _conditions(self, full_path, environ):
    mtime = os.stat(full_path).st_mtime
    size = os.stat(full_path).st_size
    return str(mtime), rfc822.formatdate(mtime), size