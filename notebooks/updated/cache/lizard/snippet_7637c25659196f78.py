def setFontUnderline(self, state):
    font = self.currentFont()
    font.setUnderline(state)
    self.setCurrentFont(font)