def _on_change(self):
    if callable(self.__callback):
        self.__callback((self._family, self._size, self._bold, self._italic,
            self._underline, self._overstrike))