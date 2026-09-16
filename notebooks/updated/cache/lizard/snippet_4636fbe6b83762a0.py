def paintEvent(self, event):
    if self.isHoverable() and self.icon().isNull():
        return
    painter = QtGui.QStylePainter()
    painter.begin(self)
    try:
        option = QtGui.QStyleOptionToolButton()
        self.initStyleOption(option)
        x_scale = 1
        y_scale = 1
        if self.flipHorizontal():
            x_scale = -1
        if self.flipVertical():
            y_scale = -1
        center = self.rect().center()
        painter.translate(center.x(), center.y())
        painter.rotate(self.angle())
        painter.scale(x_scale, y_scale)
        painter.translate(-center.x(), -center.y())
        painter.drawComplexControl(QtGui.QStyle.CC_ToolButton, option)
    finally:
        painter.end()