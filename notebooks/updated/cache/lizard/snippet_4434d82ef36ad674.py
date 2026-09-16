def update_button(self, button, widget):
    if not shiboken.isValid(widget):
        self.remove_widget(widget)
        return
    button.setIconSize(QtCore.QSize(self._iconw, self._iconh))
    pix = QtGui.QPixmap(widget.size())
    widget.render(pix)
    icon = QtGui.QIcon(pix)
    button.setIcon(icon)