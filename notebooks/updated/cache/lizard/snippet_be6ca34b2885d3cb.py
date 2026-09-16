def refresh_table(self):
    if self.is_visible and self.isVisible():
        self.shellwidget.refresh_namespacebrowser()
        try:
            self.editor.resizeRowToContents()
        except TypeError:
            pass