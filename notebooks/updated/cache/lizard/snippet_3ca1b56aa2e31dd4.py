def _on_click(self, event):
    if callable(self.__callback):
        self.__callback(self.selection)