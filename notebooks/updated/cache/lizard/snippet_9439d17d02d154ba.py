def OnReorder(self, event):
    column = self.columns[event.GetColumn()]
    return self.ReorderByColumn(column)