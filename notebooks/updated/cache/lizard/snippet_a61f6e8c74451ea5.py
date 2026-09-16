def setColor(self, color):
    self.setBorderColor(color)
    clr = QColor(color)
    clr.setAlpha(150)
    self.setHighlightColor(clr)
    clr = QColor(color)
    clr.setAlpha(80)
    self.setFillColor(clr)