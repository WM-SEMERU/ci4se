def update_grid(self, grid):
    data_methods = {'specimen': self.er_magic_data.change_specimen,
        'sample': self.er_magic_data.change_sample, 'site': self.
        er_magic_data.change_site, 'location': self.er_magic_data.
        change_location, 'age': self.er_magic_data.change_age}
    grid_name = str(grid.GetName())
    cols = list(range(grid.GetNumberCols()))
    col_labels = []
    for col in cols:
        col_labels.append(grid.GetColLabelValue(col))
    for row in grid.changes:
        if row == -1:
            continue
        else:
            data_dict = {}
            for num, label in enumerate(col_labels):
                if label:
                    data_dict[str(label)] = str(grid.GetCellValue(row, num))
            new_name = str(grid.GetCellValue(row, 0))
            old_name = self.temp_data[grid_name][row]
            data_methods[grid_name](new_name, old_name, data_dict)
    grid.changes = False