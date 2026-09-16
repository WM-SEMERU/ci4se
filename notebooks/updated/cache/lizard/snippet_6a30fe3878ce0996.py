def relative_ref(self, baseURI):
    if baseURI == '/':
        relpath = self[1:]
    else:
        relpath = posixpath.relpath(self, baseURI)
    return relpath