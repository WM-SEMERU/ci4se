def paint(self, painter, option, widget):
    if self._rebuildRequired:
        self.rebuild()
    painter.setPen(self.borderColor())
    if self.isSelected():
        painter.setBrush(self.highlightColor())
    else:
        painter.setBrush(self.fillColor())
    hints = painter.renderHints()
    if not self.isAllDay():
        painter.setRenderHint(painter.Antialiasing)
        pen = painter.pen()
        pen.setWidthF(0.25)
        painter.setPen(pen)
    painter.drawPath(self.path())
    title = self.title()
    painter.setPen(self.textColor())
    for data in self._textData:
        painter.drawText(*data)
    painter.setRenderHints(hints)