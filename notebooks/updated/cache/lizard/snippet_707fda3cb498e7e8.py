def _conditions(self, full_path, environ):
    magic = self._match_magic(full_path)
    if magic is not None:
        return magic.conditions(full_path, environ)
    else:
        mtime = stat(full_path).st_mtime
        return str(mtime), rfc822.formatdate(mtime)