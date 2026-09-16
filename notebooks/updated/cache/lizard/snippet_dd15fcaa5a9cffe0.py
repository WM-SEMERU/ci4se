def csv_column_cleaner(rows):
    result = [[] for x in range(0, len(rows))]
    for i_index in range(0, len(rows[0])):
        partial_values = []
        for x_row in rows:
            partial_values.append(x_row[i_index] if len(x_row) > i_index else
                '')
        colum_rows = exclude_empty_values(partial_values)
        if len(colum_rows) > len(rows) / 5:
            for index in range(0, len(rows)):
                result[index].append(rows[index][i_index] if len(rows[index
                    ]) > i_index else '')
    return result