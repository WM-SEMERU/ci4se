def _matrix_add_column(matrix, column, default=0):
    height_difference = len(column) - len(matrix)
    width = max(len(row) for row in matrix) if matrix else 0
    offset = 0
    if height_difference > 0:
        for _ in range(height_difference):
            matrix.insert(0, [default] * width)
    if height_difference < 0:
        offset = -height_difference
    for index, value in enumerate(column):
        row_index = index + offset
        row = matrix[row_index]
        width_difference = width - len(row)
        row.extend([default] * width_difference)
        row.append(value)