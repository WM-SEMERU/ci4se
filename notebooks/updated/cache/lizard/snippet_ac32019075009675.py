def adjustSize(self):
    align = self.closeAlignment()
    if align & QtCore.Qt.AlignTop:
        y = 6
    else:
        y = self.height() - 38
    if align & QtCore.Qt.AlignLeft:
        x = 6
    else:
        x = self.width() - 38
    self._closeButton.move(x, y)
    widget = self.centralWidget()
    if widget is not None:
        center = self.rect().center()
        widget.move(center.x() - widget.width() / 2, center.y() - widget.
            height() / 2)