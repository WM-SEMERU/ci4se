def open_fileswitcher(self, symbol=False):
    if self.fileswitcher is not None and self.fileswitcher.is_visible:
        self.fileswitcher.hide()
        self.fileswitcher.is_visible = False
        return
    if symbol:
        self.fileswitcher.plugin = self.editor
        self.fileswitcher.set_search_text('@')
    else:
        self.fileswitcher.set_search_text('')
    self.fileswitcher.show()
    self.fileswitcher.is_visible = True