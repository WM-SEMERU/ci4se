def add_codewords(matrix, codewords, version):
    matrix_size = len(matrix)
    is_micro = version < 1
    inc = 0 if version not in (consts.VERSION_M1, consts.VERSION_M3) else 2
    idx = 0
    for right in range(matrix_size - 1, 0, -2):
        if not is_micro and right <= 6:
            right -= 1
        for vertical in range(matrix_size):
            for z in range(2):
                j = right - z
                upwards = right + inc & 2 == 0
                if not is_micro:
                    upwards ^= j < 6
                i = matrix_size - 1 - vertical if upwards else vertical
                if matrix[i][j] == 2 and idx < len(codewords):
                    matrix[i][j] = codewords[idx]
                    idx += 1
    if idx != len(codewords):
        raise QRCodeError(
            'Internal error: Adding codewords to matrix failed. Added {0} of {1} codewords'
            .format(idx, len(codewords)))