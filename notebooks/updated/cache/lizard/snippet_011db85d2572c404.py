def close(self):
    if not self._closed:
        self.__flush()
        object.__setattr__(self, '_closed', True)