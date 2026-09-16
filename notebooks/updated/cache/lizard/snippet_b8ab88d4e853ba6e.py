def drawCheck(self, painter, option, rect, state):
    if not self.useCheckMaps():
        return super(XTreeWidgetDelegate, self).drawCheck(painter, option,
            rect, state)
    pixmap = None
    if state == QtCore.Qt.Checked:
        pixmap = self.checkOnMap()
    elif state == QtCore.Qt.PartiallyChecked:
        pixmap = self.checkPartialMap()
    elif state == QtCore.Qt.Unchecked:
        pixmap = self.checkOffMap()
    if type(pixmap) in (str, unicode):
        pixmap = QtGui.QPixmap(pixmap)
    if not pixmap:
        return
    x = rect.x() + (rect.width() - 16) / 2.0
    y = rect.y() + (rect.height() - 16) / 2.0
    painter.drawPixmap(int(x), int(y), pixmap)