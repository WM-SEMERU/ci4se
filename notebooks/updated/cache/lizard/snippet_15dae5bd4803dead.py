def addPixmap(self, pixmap):
    item = QtGui.QGraphicsPixmapItem(pixmap)
    self.addToGroup(item)
    return item