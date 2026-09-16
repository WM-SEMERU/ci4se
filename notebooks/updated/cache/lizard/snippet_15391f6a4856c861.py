def addPixmap(self, pixmap):
    scene = self.scene()
    scene.addItem(XImageItem(pixmap))
    self.recalculate()