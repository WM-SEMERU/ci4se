def OnCellBackgroundColor(self, event):
    with undo.group(_('Background color')):
        self.grid.actions.set_attr('bgcolor', event.color)
    self.grid.ForceRefresh()
    self.grid.update_attribute_toolbar()
    event.Skip()