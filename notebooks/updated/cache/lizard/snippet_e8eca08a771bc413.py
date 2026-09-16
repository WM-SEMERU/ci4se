def _handleEsc(self):
    if self._typingSms:
        self.serial.write(self.ESC_CHARACTER)
        self._typingSms = False
        self.inputBuffer = []
        self.cursorPos = 0