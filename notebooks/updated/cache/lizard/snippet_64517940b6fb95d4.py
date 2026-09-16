def add_row(self, label='', item=''):
    self.AppendRows(1)
    last_row = self.GetNumberRows() - 1
    self.SetCellValue(last_row, 0, str(label))
    self.row_labels.append(label)
    self.row_items.append(item)