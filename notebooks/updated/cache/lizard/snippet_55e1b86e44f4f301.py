def currentPixmapRect(self):
    pixmap = self.currentPixmap()
    rect = self.rect()
    size = pixmap.size()
    x = rect.center().x() - size.width() / 2.0
    y = rect.center().y() - size.height() / 2.0
    return QtCore.QRect(x, y, size.width(), size.height())