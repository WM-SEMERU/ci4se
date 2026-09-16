def drawGrid(self, painter, opt, rect, index):
    if not self.showGrid():
        return
    painter.setBrush(QtCore.Qt.NoBrush)
    painter.setPen(self.gridPen())
    size = self.gridPen().width() + 1
    lines = []
    if self.showGridColumns():
        lines.append(QtCore.QLine(rect.width() - size, 0, rect.width() -
            size, rect.height() - size))
    if self.showGridRows():
        lines.append(QtCore.QLine(0, rect.height() - size, rect.width() -
            size, rect.height() - size))
    painter.drawLines(lines)