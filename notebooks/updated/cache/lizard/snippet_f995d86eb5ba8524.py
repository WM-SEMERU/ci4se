def resizeEvent(self, event):
    super(XNavigationEdit, self).resizeEvent(event)
    w = self.width()
    h = self.height()
    self._scrollWidget.resize(w - 4, h - 4)
    if self._scrollWidget.width() < self._partsWidget.width():
        self.scrollParts(self._partsWidget.width() - self._scrollWidget.width()
            )