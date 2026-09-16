def setupSplash(self, pixmap, align=None, color='white', cls=None):
    if cls is None:
        cls = XLoggerSplashScreen
    if align is None:
        align = QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom
    color = QtGui.QColor('white')
    pixmap = QtGui.QPixmap(pixmap)
    screen = cls(splash)
    screen.setTextColor(color)
    screen.setTextAlignment(align)
    screen.show()
    self.processEvents()
    self._splash = screen
    return screen