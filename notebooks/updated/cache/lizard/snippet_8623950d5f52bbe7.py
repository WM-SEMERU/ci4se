def set_artist(self, artist):
    self._set_attr(TPE1(encoding=3, text=artist.decode('utf-8')))