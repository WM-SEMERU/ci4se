def update(self, render, force=False):
    if not force and not self._needUpdate:
        return
    self._needUpdate = False
    i = 0
    drawArea = QtGui.QImage(self._width, self._height, render.getImageFormat())
    drawArea.fill(self._backgroudColor)
    with QtGui.QPainter(drawArea) as qp:
        for label in self._labels:
            rect = QtCore.QRect(0, i * self._cellHeight, self._width - 2,
                self._cellHeight)
            if i == self._current:
                qp.setPen(QtCore.Qt.darkGreen)
                qp.drawRoundedRect(rect, 5.0, 5.0)
            qp.setPen(QtCore.Qt.white)
            qp.setFont(QtGui.QFont('arial', self._fontSize, QtGui.QFont.Bold))
            qp.drawText(rect, QtCore.Qt.AlignCenter, label)
            i += 1
    render.drawImage(drawArea)