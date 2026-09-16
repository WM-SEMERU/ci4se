def _evaluate_hodograph(s, nodes):
    r
    _, num_nodes = np.shape(nodes)
    first_deriv = nodes[:, 1:] - nodes[:, :-1]
    return (num_nodes - 1) * evaluate_multi(first_deriv, np.asfortranarray([s])
        )