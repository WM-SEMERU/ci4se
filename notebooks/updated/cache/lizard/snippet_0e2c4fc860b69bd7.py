def read_node_label_matrix(file_path, separator, numbering='matlab'):
    file_row_generator = get_file_row_generator(file_path, separator)
    file_row = next(file_row_generator)
    number_of_rows = file_row[1]
    number_of_categories = int(file_row[3])
    row = list()
    col = list()
    append_row = row.append
    append_col = col.append
    for file_row in file_row_generator:
        node = np.int64(file_row[0])
        label = np.int64(file_row[1])
        append_row(node)
        append_col(label)
    labelled_node_indices = np.array(list(set(row)))
    row = np.array(row, dtype=np.int64)
    col = np.array(col, dtype=np.int64)
    data = np.ones_like(row, dtype=np.float64)
    if numbering == 'matlab':
        row -= 1
        col -= 1
        labelled_node_indices -= 1
    elif numbering == 'c':
        pass
    else:
        print('Invalid numbering style.')
        raise RuntimeError
    node_label_matrix = spsp.coo_matrix((data, (row, col)), shape=(
        number_of_rows, number_of_categories))
    node_label_matrix = node_label_matrix.tocsr()
    return node_label_matrix, number_of_categories, labelled_node_indices