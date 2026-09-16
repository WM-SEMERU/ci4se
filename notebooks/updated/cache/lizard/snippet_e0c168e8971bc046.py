def solve_assignement(self, costs):
    if costs is None or len(costs) == 0:
        return dict()
    n = costs.shape[0]
    pairs = [(i, j) for i in range(0, n) for j in range(0, n) if costs[i, j
        ] < invalid_match]
    costs_list = [costs[i, j] for i, j in pairs]
    assignment = lapjv.lapjv(list(zip(*pairs))[0], list(zip(*pairs))[1],
        costs_list)
    indexes = enumerate(list(assignment[0]))
    return dict([(row, col) for row, col in indexes])