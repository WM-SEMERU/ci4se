def get_mimetype(self, path):
    for fnc in self._mimetype_functions:
        mime = fnc(path)
        if mime:
            return mime
    return mimetype.by_default(path)