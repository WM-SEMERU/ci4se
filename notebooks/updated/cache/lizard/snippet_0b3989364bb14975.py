def _add_column(self, label, field):
    assert self.headers is not None
    cols = 0
    if len(self._headers) > 0:
        cols = max([int(c.cell.col) for c in self._headers])
    new_col = cols + 1
    if int(self._ws.col_count.text) < new_col:
        self._ws.col_count.text = str(new_col)
        self._update_metadata()
    cell = self._service.UpdateCell(1, new_col, label, self._ss.id, self.id)
    self._headers.append(cell)