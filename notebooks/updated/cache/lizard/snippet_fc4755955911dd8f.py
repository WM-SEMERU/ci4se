def drawAxis(self, painter):
    pen = QPen(self.axisColor())
    pen.setWidth(4)
    painter.setPen(pen)
    painter.drawLines(self._buildData['axis_lines'])
    for rect, text in self._buildData['grid_h_notches']:
        painter.drawText(rect, Qt.AlignTop | Qt.AlignRight, text)
    for rect, text in self._buildData['grid_v_notches']:
        painter.drawText(rect, Qt.AlignCenter, text)