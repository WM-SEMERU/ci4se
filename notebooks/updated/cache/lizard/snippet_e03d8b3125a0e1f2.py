def generate_poisson_lineage(n_states, n_cells_per_cluster, n_genes, means=300
    ):
    M = np.random.random((n_genes, n_states)) * means
    center = M.mean(1)
    W = np.zeros((n_states, n_cells_per_cluster * n_states))
    index = 0
    means = np.array([1.0 / n_states] * n_states)
    for c in range(n_states):
        for i in range(n_cells_per_cluster):
            w = np.copy(means)
            new_value = w[c] + i * (1.0 - 1.0 / n_states) / n_cells_per_cluster
            w[:] = (1.0 - new_value) / (n_states - 1.0)
            w[c] = new_value
            W[:, (index)] = w
            index += 1
    return M, W