def retrieve_csv_data(rows, row_header=0, column_header=0, limit_column=0):
    return [row[row_header:limit_column] for row in rows[column_header:]]