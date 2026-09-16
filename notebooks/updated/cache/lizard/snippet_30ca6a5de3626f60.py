def OnQuote(self, event):
    grid = self.grid
    grid.DisableCellEditControl()
    with undo.group(_('Quote cell(s)')):
        if self.grid.IsSelection():
            self.grid.actions.quote_selection()
            self.grid.ForceRefresh()
        else:
            row = self.grid.GetGridCursorRow()
            col = self.grid.GetGridCursorCol()
            key = row, col, grid.current_table
            self.grid.actions.quote_code(key)
            grid.MoveCursorDown(False)