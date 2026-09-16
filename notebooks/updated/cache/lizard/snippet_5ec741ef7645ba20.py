def has_header_line(self, key, id_):
    if key not in self._indices:
        return False
    else:
        return id_ in self._indices[key]