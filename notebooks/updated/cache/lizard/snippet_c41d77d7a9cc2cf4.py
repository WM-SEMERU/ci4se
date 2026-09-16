def OnRangeSelected(self, event):
    if not self.grid.IsEditable():
        selection = self.grid.selection
        row, col, __ = self.grid.sel_mode_cursor
        if (row, col) in selection:
            self.grid.ClearSelection()
        else:
            self.grid.SetGridCursor(row, col)
            post_command_event(self.grid, self.grid.SelectionMsg, selection
                =selection)