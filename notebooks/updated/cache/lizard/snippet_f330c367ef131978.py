def hide(self):
    for widget in self.replace_widgets:
        widget.hide()
    QWidget.hide(self)
    self.visibility_changed.emit(False)
    if self.editor is not None:
        self.editor.setFocus()
        self.clear_matches()