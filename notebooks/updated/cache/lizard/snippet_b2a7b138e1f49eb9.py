def _get(self, key):
    buf = BytesIO()
    self._get_file(key, buf)
    return buf.getvalue()