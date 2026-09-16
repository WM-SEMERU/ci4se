def _populate_random_tournament_row_col(n, r, row, col):
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if r[k] < 0.5:
                row[k], col[k] = i, j
            else:
                row[k], col[k] = j, i
            k += 1