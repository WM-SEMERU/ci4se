def OnTableChanged(self, event):
    if hasattr(event, 'table'):
        self.Select(event.table)
        self.EnsureVisible(event.table)
    event.Skip()