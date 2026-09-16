def update_cells(self, cell_list, value_input_option='RAW'):
    values_rect = cell_list_to_rect(cell_list)
    start = rowcol_to_a1(min(c.row for c in cell_list), min(c.col for c in
        cell_list))
    end = rowcol_to_a1(max(c.row for c in cell_list), max(c.col for c in
        cell_list))
    range_label = '%s!%s:%s' % (self.title, start, end)
    data = self.spreadsheet.values_update(range_label, params={
        'valueInputOption': value_input_option}, body={'values': values_rect})
    return data