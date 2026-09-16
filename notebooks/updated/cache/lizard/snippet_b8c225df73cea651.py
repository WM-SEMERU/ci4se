def apply_mask(matrix, mask_pattern, matrix_size, is_encoding_region):
    for i in range(matrix_size):
        for j in range(matrix_size):
            if is_encoding_region(i, j):
                matrix[i][j] ^= mask_pattern(i, j)