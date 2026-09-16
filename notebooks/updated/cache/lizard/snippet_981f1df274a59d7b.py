def delta(x_i, j, s, N):
    flag = j == EMMMixPLAggregator.c(x_i, s)
    if flag and s < len(x_i):
        return 1
    elif s == N:
        found_equal = False
        for l in range(len(x_i)):
            if j == EMMMixPLAggregator.c(x_i, l):
                found_equal = True
                break
        if not found_equal:
            return 1
    return 0