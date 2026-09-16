def addText(self, text, width=None):
    item = QtGui.QGraphicsTextItem()
    font = item.font()
    font.setFamily('Arial')
    font.setPointSize(12)
    item.setFont(font)
    item.setHtml(text)
    item.setDefaultTextColor(QtGui.QColor('white'))
    self.addToGroup(item)
    item.graphicsEffect().setBlurRadius(8)
    if width:
        item.setTextWidth(width)
    return item