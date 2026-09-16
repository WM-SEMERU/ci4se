def _qnwsimp1(n, a, b):
    if n % 2 == 0:
        print('WARNING qnwsimp: n must be an odd integer. Increasing by 1')
        n += 1
    nodes = np.linspace(a, b, n)
    dx = nodes[1] - nodes[0]
    weights = np.kron(np.ones((n + 1) // 2), np.array([2.0, 4.0]))
    weights = weights[:n]
    weights[0] = weights[-1] = 1
    weights = dx / 3.0 * weights
    return nodes, weights