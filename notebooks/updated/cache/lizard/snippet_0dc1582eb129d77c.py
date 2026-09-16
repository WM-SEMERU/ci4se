def isIn(row, col_name, arg, dm, df, con=None):
    cell_value = row[col_name]
    cell_value = str(cell_value)
    if not cell_value:
        return None
    elif cell_value == 'None':
        return None
    elif cell_value == 'nan':
        return None
    elif not con:
        return None
    cell_values = [v.strip(' ') for v in cell_value.split(':')]
    if '.' in arg:
        table_name, table_col_name = arg.split('.')
        if table_name not in con.tables:
            return None
        if table_col_name not in con.tables[table_name].df.columns:
            return (
                '{} table is missing "{}" column, which is required for validating "{}" column'
                .format(table_name, table_col_name, col_name))
        possible_values = con.tables[table_name].df[table_col_name].unique()
        for value in cell_values:
            if value not in possible_values:
                trunc_possible_values = [val.replace(' ', '') for val in
                    possible_values if val]
                trunc_cell_value = cell_value.replace(' ', '')
                if trunc_cell_value not in trunc_possible_values:
                    if trunc_cell_value != value:
                        return (
                            'This value (long): "{}" is not found in: {} column in {} table.  Also (short): {} is not in {}'
                            .format(value, table_col_name, table_name,
                            trunc_cell_value, arg))
                    else:
                        return (
                            'This value: "{}" is not found in: {} column in {} table'
                            .format(value, table_col_name, table_name))
                    break
    else:
        possible_values = df[arg].unique()
        for value in cell_values:
            if value not in possible_values:
                return 'This value: "{}" is not found in: {} column'.format(
                    value, arg)
                break
    return None