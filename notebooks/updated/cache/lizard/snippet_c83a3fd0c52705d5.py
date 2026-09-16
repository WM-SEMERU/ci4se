def foreground(self):
    widget = self.widget()
    if widget:
        palette = widget.palette()
        return palette.color(palette.WindowText)
    else:
        return QtGui.QColor()