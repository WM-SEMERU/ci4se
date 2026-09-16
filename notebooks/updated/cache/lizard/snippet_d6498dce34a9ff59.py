def show(self):
    if self.isHidden():
        QWidget.show(self)
        self._qpart.updateViewport()