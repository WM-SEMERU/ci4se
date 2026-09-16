def OnCellBorderWidth(self, event):
    with undo.group(_('Border width')):
        self.grid.actions.set_border_attr('borderwidth', event.width, event
            .borders)
    self.grid.ForceRefresh()
    self.grid.update_attribute_toolbar()
    event.Skip()