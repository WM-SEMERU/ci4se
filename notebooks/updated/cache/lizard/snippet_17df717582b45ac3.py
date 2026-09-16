def native(self):
    if self.contents is None:
        return None
    if self._parsed is not None:
        return self._parsed[0].native
    else:
        return self.__bytes__()