def score_n1(matrix, matrix_size):
    score = 0
    for i in range(matrix_size):
        prev_bit_row, prev_bit_col = -1, -1
        row_counter, col_counter = 0, 0
        for j in range(matrix_size):
            bit = matrix[i][j]
            if bit == prev_bit_row:
                row_counter += 1
            else:
                if row_counter >= 5:
                    score += row_counter - 2
                row_counter = 1
                prev_bit_row = bit
            bit = matrix[j][i]
            if bit == prev_bit_col:
                col_counter += 1
            else:
                if col_counter >= 5:
                    score += col_counter - 2
                col_counter = 1
                prev_bit_col = bit
        if row_counter >= 5:
            score += row_counter - 2
        if col_counter >= 5:
            score += col_counter - 2
    return score