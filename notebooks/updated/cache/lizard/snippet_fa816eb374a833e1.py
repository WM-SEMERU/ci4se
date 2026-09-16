def populate_csv_headers(rows, partial_headers, column_headers_count=1):
    result = [''] * (len(rows) - column_headers_count)
    for i_index in range(0, len(partial_headers)):
        for k_index in range(0, len(partial_headers[i_index])):
            if not partial_headers[i_index][k_index] and i_index - 1 >= 0:
                for t_index in range(i_index - 1, -1, -1):
                    partial_value = partial_headers[t_index][k_index]
                    if partial_value:
                        partial_headers[i_index][k_index] = partial_value
                        break
        result[i_index] = ' '.join(map(str, partial_headers[i_index]))
    return result