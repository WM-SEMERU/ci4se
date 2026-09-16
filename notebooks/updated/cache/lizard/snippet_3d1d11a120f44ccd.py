def paintEvent(self, event):
    pen = QPen(Qt.DashLine)
    pen.setColor(QColor('red'))
    with XPainter(self) as painter:
        painter.setPen(pen)
        clr = QColor('black')
        clr.setAlpha(100)
        painter.setBrush(clr)
        painter.drawRect(self._region)