def get_position(self):
    pos = QtGui.QCursor.pos()
    if self._alignment & QtCore.Qt.AlignLeft == QtCore.Qt.AlignLeft:
        pos.setX(pos.x() - self._offset)
    elif self._alignment & QtCore.Qt.AlignRight == QtCore.Qt.AlignRight:
        pos.setX(pos.x() - self.frameGeometry().width() + self._offset)
    elif self._alignment & QtCore.Qt.AlignHCenter == QtCore.Qt.AlignHCenter:
        pos.setX(pos.x() - self.frameGeometry().width() / 2)
    if self._alignment & QtCore.Qt.AlignTop == QtCore.Qt.AlignTop:
        pos.setY(pos.y() - self._offset)
    elif self._alignment & QtCore.Qt.AlignBottom == QtCore.Qt.AlignBottom:
        pos.setY(pos.y() - self.frameGeometry().height() + self._offset)
    elif self._alignment & QtCore.Qt.AlignVCenter == QtCore.Qt.AlignVCenter:
        pos.setY(pos.y() - self.frameGeometry().height() / 2)
    return pos