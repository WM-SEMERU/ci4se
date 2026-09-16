def generate_nb_states(n_states, n_cells, n_genes):
    W = np.random.dirichlet([1] * n_states, size=(n_cells,))
    W = W.T
    M = np.random.random((n_genes, n_states)) * 100
    R = np.random.randint(1, 100, n_genes)
    return M, W, R