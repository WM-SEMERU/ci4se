def ext(self):
    raw_ext = posixpath.splitext(self)[1]
    return raw_ext[1:] if raw_ext.startswith('.') else raw_ext