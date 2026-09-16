def _populate_sgc_payoff_arrays(payoff_arrays):
    n = payoff_arrays[0].shape[0]
    m = (n + 1) // 2 - 1
    for payoff_array in payoff_arrays:
        for i in range(m):
            for j in range(m):
                payoff_array[i, j] = 0.75
            for j in range(m, n):
                payoff_array[i, j] = 0.5
        for i in range(m, n):
            for j in range(n):
                payoff_array[i, j] = 0
        payoff_array[0, m - 1] = 1
        payoff_array[0, 1] = 0.5
        for i in range(1, m - 1):
            payoff_array[i, i - 1] = 1
            payoff_array[i, i + 1] = 0.5
        payoff_array[m - 1, m - 2] = 1
        payoff_array[m - 1, 0] = 0.5
    k = (m + 1) // 2
    for h in range(k):
        i, j = m + 2 * h, m + 2 * h
        payoff_arrays[0][i, j] = 0.75
        payoff_arrays[0][i + 1, j + 1] = 0.75
        payoff_arrays[1][j, i + 1] = 0.75
        payoff_arrays[1][j + 1, i] = 0.75