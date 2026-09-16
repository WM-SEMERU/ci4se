def make_worksheet(self, sheet_name=None):
    if sheet_name is None:
        sheet_name = self.table_name
    if not sheet_name:
        sheet_name = ''
    self._stream = self.workbook.add_worksheet(sheet_name)
    self._current_data_row = self._first_data_row