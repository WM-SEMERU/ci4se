def OnPasteFormat(self, event):
    with undo.group(_('Paste format')):
        self.grid.actions.paste_format()
    self.grid.ForceRefresh()
    self.grid.update_attribute_toolbar()
    self.grid.actions.zoom()