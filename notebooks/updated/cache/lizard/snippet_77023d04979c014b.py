def get_chron_var(temp_sheet, start_row):
    col_dict = OrderedDict()
    out_list = []
    column = 1
    while temp_sheet.cell_value(start_row, 0
        ) != '' and start_row < temp_sheet.nrows:
        short_cell = temp_sheet.cell_value(start_row, 0)
        units_cell = temp_sheet.cell_value(start_row, 1)
        long_cell = temp_sheet.cell_value(start_row, 2)
        col_dict['number'] = column
        col_dict['variableName'] = short_cell
        col_dict['description'] = long_cell
        col_dict['units'] = units_cell
        out_list.append(col_dict.copy())
        start_row += 1
        column += 1
    return out_list