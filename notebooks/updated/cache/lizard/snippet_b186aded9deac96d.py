def paintEvent(self, event):
    super(AutoParameterTableView, self).paintEvent(event)
    if self.dragline is not None:
        pen = QtGui.QPen(QtCore.Qt.blue)
        painter = QtGui.QPainter(self.viewport())
        painter.setPen(pen)
        painter.drawLine(self.dragline)