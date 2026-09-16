def chi_square_calc(classes, table, TOP, P, POP):
    try:
        result = 0
        for i in classes:
            for index, j in enumerate(classes):
                expected = TOP[j] * P[i] / POP[i]
                result += (table[i][j] - expected) ** 2 / expected
        return result
    except Exception:
        return 'None'