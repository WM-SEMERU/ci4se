def calculateSceneWidth(self):
    widths = []
    w = self.width() / 2.0
    h = self.height() / 2.0
    for item in self.scene().items():
        pixmap = item.basePixmap()
        thumb = pixmap.scaled(pixmap.width(), h, Qt.KeepAspectRatio)
        widths.append(thumb.width())
        item.setPixmap(thumb)
    return sum(widths) + self.spacing() * (self.count() - 1) + w