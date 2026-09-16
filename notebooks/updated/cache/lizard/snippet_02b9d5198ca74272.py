def evaluate_mask(matrix, matrix_size):
    return score_n1(matrix, matrix_size) + score_n2(matrix, matrix_size
        ) + score_n3(matrix, matrix_size) + score_n4(matrix, matrix_size)