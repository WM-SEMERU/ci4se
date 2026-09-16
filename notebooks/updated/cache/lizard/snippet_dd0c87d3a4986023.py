def switchDisplay(self, display):
    if display in self.displays:
        self.setWidget(self.displays[display])
        self._current = display
    else:
        raise Exception('Undefined display type ' + display)